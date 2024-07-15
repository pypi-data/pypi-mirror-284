import logging
from datetime import datetime
from decimal import Decimal

from delta import DeltaTable
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import current_timestamp, expr, lit
from pyspark.sql.types import Any, DateType, DecimalType, IntegerType, StringType, TimestampType

from fabric_fast_start.FabricContext import FabricContext
from fabric_fast_start.Logger import Logger


class DeltaTableManager:

    AUDIT_COLUMNS = {
        "SCD1": {"updated_date": "_updated_at", "updated_by": "_updated_by"},
        "SCD2": {"created_date": "_created_at", "effective_date": "_start_date", "end_date": "_end_date", "is_current": "_is_current"},
    }

    def __init__(self, fabric_context: FabricContext, table_name: str, debug: bool = False):
        self._logger = Logger.setup_logger(self.__class__.__name__, logging.DEBUG if debug else logging.INFO)
        self._spark = fabric_context.spark
        self.table_name = table_name
        self.table_path = f"tmp/{table_name}"
        self.end_time = datetime(9999, 12, 31)

    @property
    def spark(self) -> SparkSession:
        return self._spark

    @property
    def logger(self) -> Logger:
        return self._logger

    def create_table(self, source_data: DataFrame, merge_type, add_unknown_record: bool = True):
        # initial_data = self.spark.createDataFrame(source_data, source_data.schema)
        if add_unknown_record:
            self.logger.info("Data prepared, starting merge operation.")
            unknown_data = [self._default_value(field.dataType) for field in source_data.schema.fields]
            # Use parallelize to handle None values properly
            unknown_record = self.spark.createDataFrame([tuple(unknown_data)], schema=source_data.schema)
        else:
            unknown_record = self.spark.createDataFrame([], source_data.schema)
        initial_data = unknown_record.union(source_data)
        prepared_data = self.prepare_data(initial_data, "SCD2" if merge_type == "scd2" else "SCD1")
        prepared_data.write.format("delta").mode("overwrite").save(self.table_path)
        self.logger.info("Delta table created or recreated successfully at: " + self.table_path)

    def update_table(self, df: DataFrame, merge_type, primary_keys, tracked_columns=None):
        delta_table = DeltaTable.forPath(self.spark, self.table_path)
        prepared_data = self.prepare_data(df, "SCD2" if merge_type == "scd2" else "SCD1")
        if merge_type.lower() == "scd1":
            self._merge_scd1(delta_table, prepared_data, primary_keys)
        elif merge_type.lower() == "scd2":
            self._merge_scd2(delta_table, prepared_data, primary_keys, tracked_columns)
        else:
            raise ValueError(f"Unsupported merge type specified: {merge_type}")

    def get_delta_table(self):
        return DeltaTable.forPath(self.spark, self.table_path)

    def table_exists(self):
        return self.spark.catalog.tableExists(self.table_name)

    def get_table(self):
        return self.spark.read.format("delta").load(self.table_path)

    def _default_value(self, data_type: Any) -> Any:
        if isinstance(data_type, StringType):
            return "Unknown"
        elif isinstance(data_type, DecimalType):
            return Decimal("0.000000")
        elif isinstance(data_type, IntegerType):
            return 0
        elif isinstance(data_type, DateType):
            # Use a datetime.date object directly suitable for DateType
            return datetime.strptime("1970-01-01", "%Y-%m-%d").date()
        elif isinstance(data_type, TimestampType):
            # Use a datetime object directly suitable for TimestampType
            return datetime.strptime("1970-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
        return "N/A"

    def prepare_data(self, source_data: DataFrame, audit_type: str = "SCD2") -> DataFrame:
        """
        Prepare data by adding audit columns and optionally an unknown record.

        :param source_data: The source DataFrame.
        :param audit_type: Type of audit (SCD1 or SCD2) to apply.
        :return: A DataFrame with the necessary audit columns added.
        """
        if audit_type not in self.AUDIT_COLUMNS:
            raise ValueError(f"Unsupported audit type: {audit_type}")
        audit_info = self.AUDIT_COLUMNS[audit_type]

        for col_name, alias in audit_info.items():
            if col_name in ["created_date", "updated_date", "effective_date"]:
                source_data = source_data.withColumn(alias, lit(current_timestamp()))
            elif col_name == "end_date":
                source_data = source_data.withColumn(alias, lit(datetime(9999, 12, 31)))
            elif col_name == "is_current":
                source_data = source_data.withColumn(alias, lit(True))
            else:
                source_data = source_data.withColumn(alias, lit("System"))

        self.logger.info(f"Audit columns added under {audit_type} configuration")
        self.logger.debug(f"source_data schema: {source_data.schema}")
        return source_data

    def _merge_scd1(self, delta_table, df: DataFrame, primary_keys):
        merge_condition = " AND ".join([f"target.{pk} = source.{pk}" for pk in primary_keys])
        delta_table.alias("target").merge(df.alias("source"), merge_condition).whenMatchedUpdateAll().whenNotMatchedInsertAll().execute()
        self.logger.info("SCD Type 1 merge executed successfully.")

    def _merge_scd2(self, delta_table, df: DataFrame, primary_keys, tracked_columns):
        current_time = current_timestamp()
        merge_condition = " AND ".join([f"target.{pk} = source.{pk}" for pk in primary_keys]) + " AND target.is_current = true"

        delta_table.alias("target").merge(df.alias("source"), merge_condition).whenMatchedUpdate(
            condition=expr(" OR ".join([f"target.{col} <> source.{col}" for col in tracked_columns])), set={"end_date": current_time, "is_current": lit(False)}
        ).execute()

        insert_columns = {col: f"source.{col}" for col in df.columns}
        insert_columns.update({"start_date": current_time, "end_date": lit(None).cast(TimestampType()), "is_current": lit(True)})  # type: ignore

        delta_table.alias("target").merge(df.alias("source"), "target.is_current = false").whenNotMatchedInsert(values=insert_columns).execute()

        self.logger.info("SCD Type 2 merge executed successfully.")
