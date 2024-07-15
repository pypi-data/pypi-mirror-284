import logging

from pyspark.sql import DataFrame
from pyspark.sql.types import StructType

from fabric_fast_start.dw.DeltaTableManager import DeltaTableManager
from fabric_fast_start.FabricContext import FabricContext
from fabric_fast_start.Logger import Logger


class DwDimensionManager:
    def __init__(self, fabric_context: FabricContext, delta_table_name: str, schema: StructType, debug: bool = False):
        self.logger = Logger.setup_logger(self.__class__.__name__, logging.DEBUG if debug else logging.INFO)
        self.table_manager = DeltaTableManager(fabric_context, delta_table_name)

    def execute_merge(self, source_data: DataFrame, merge_type: str, primary_keys: list[str], tracked_columns: list[str] = []):
        """
        Prepare and execute a merge operation on the Delta table.

        :param source_data: The source DataFrame to be merged.
        :param merge_type: Type of merge (SCD1 or SCD2).
        :param primary_keys: Primary keys to identify records.
        :param tracked_columns: Columns to track for changes (needed for SCD2).
        """
        self.logger.info(f"Preparing data for {merge_type} merge.")
        # Check if df is None or has no schema
        if source_data is None or source_data.schema is None:
            raise ValueError("DataFrame is None or does not have a schema.")

        # create table if not exists
        if not self.table_manager.table_exists():
            self.table_manager.create_table(source_data, merge_type, add_unknown_record=True)
        self.table_manager.update_table(source_data, merge_type, primary_keys, tracked_columns)
        # self.table_manager.save_delta_table()
        self.logger.info("Merge operation completed successfully.")
