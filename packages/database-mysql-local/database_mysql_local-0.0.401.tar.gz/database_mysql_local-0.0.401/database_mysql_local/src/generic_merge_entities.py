import datetime
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from .generic_crud_ml import GenericCRUDML
DEFAULT_LIMIT = 5
DEFAULT_ORDER_BY = "updated_timestamp DESC"
LOGGER_MINIMUM_SEVERITY="Info"

class MergeEntities (GenericCRUDML):
    def merge_entities(self, schema_name: str, table_name: str, entity_id1: int, entity_id2: int, main_entity_ml_id: int = None):
        table_prefix = table_name[:-6]
        generated_ml_table_name = table_prefix + '_ml_table'
        generated_ml_view_name = table_prefix + '_ml_view'
        generated_table_name = table_prefix + '_table'
        gcrml = GenericCRUDML(default_schema_name=schema_name, default_ml_table_name=generated_ml_table_name,is_test_data=True, default_table_name=generated_table_name, default_ml_view_table_name= generated_ml_view_name)
        # establish which id is being merged/ended and which one it is being merged into
        end_id = entity_id1
        main_id = entity_id2

        # Data to update
        old_id = end_id
        new_id = main_id
        #get the ml ids of the city id which is being merged

        generated_ml_column_name = table_prefix + '_ml_id'
        generated_column_name = table_prefix + '_id'
        mlids = gcrml.get_all_ml_ids_by_id(table_id=old_id,ml_column_name=generated_ml_column_name,order_by=DEFAULT_ORDER_BY, ml_table_name=generated_ml_table_name, column_name=generated_column_name, compare_view_name=generated_ml_view_name)

        # Set the main id
        if main_entity_ml_id is not None:
            gcrml.update_by_column_and_value(
                table_name=generated_ml_table_name,
                column_name=generated_ml_column_name,
                column_value=main_entity_ml_id,
                data_dict={'is_main': True },)
        for id in mlids:
            name = gcrml.select_one_value_by_column_and_value(
                select_clause_value = 'title',
                schema_name=schema_name,
                view_table_name=generated_ml_view_name,
                column_name=generated_ml_column_name,
                column_value=id,
            )
            gcrml.update_by_column_and_value(
                table_name=generated_ml_table_name,
                column_name=generated_ml_column_name,
                column_value=id,
                data_dict={generated_column_name: new_id,}
            )

        gcrml.update_by_column_and_value(
        table_name=generated_table_name,
        column_name=generated_column_name,
        column_value=old_id,
        data_dict={"end_timestamp": datetime.datetime.now()},
    )














