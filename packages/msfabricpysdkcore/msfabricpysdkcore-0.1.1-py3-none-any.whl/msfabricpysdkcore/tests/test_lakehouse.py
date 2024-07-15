import unittest
from datetime import datetime
from dotenv import load_dotenv
from time import sleep
from msfabricpysdkcore.coreapi import FabricClientCore

load_dotenv()

class TestFabricClientCore(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestFabricClientCore, self).__init__(*args, **kwargs)
        #load_dotenv()
        self.fc = FabricClientCore()
        self.workspace_id = "c3352d34-0b54-40f0-b204-cc964b1beb8d"

        datetime_str = datetime.now().strftime("%Y%m%d%H%M%S")
        self.item_name = "testitem" + datetime_str
        self.item_type = "Notebook"

    def test_lakehouse(self):

        lakehouse = self.fc.get_item(workspace_id=self.workspace_id, item_name="lakehouse1", item_type="Lakehouse")
        self.assertIsNotNone(lakehouse.properties)
        lakehouse_id = lakehouse.id
        workspace_id = self.workspace_id
        date_str = datetime.now().strftime("%Y%m%d%H%M%S")
        table_name = f"table{date_str}"


        status_code = self.fc.load_table(workspace_id=self.workspace_id, lakehouse_id=lakehouse_id, table_name=table_name, 
                                         path_type="File", relative_path="Files/folder1/titanic.csv")

        self.assertEqual(status_code, 202)

        # Run on demand table maintenance
        table_name_maintenance = "table20240515114529"

        execution_data = {
            "tableName": table_name_maintenance,
            "optimizeSettings": {
            "vOrder": True,
            "zOrderBy": [
                "tipAmount"
            ]
            },
            "vacuumSettings": {
            "retentionPeriod": "7:01:00:00"
            }
        }
        
        response = self.fc.run_on_demand_table_maintenance(workspace_id=workspace_id, lakehouse_id=lakehouse_id, 
                                                           execution_data = execution_data,
                                                           job_type = "TableMaintenance", wait_for_completion = False)
        self.assertIn(response.status_code, [200, 202])

        table_list = self.fc.list_tables(workspace_id=self.workspace_id, lakehouse_id=lakehouse_id)
        table_names = [table["name"] for table in table_list]

        self.assertIn(table_name, table_names)

        fc = self.fc
        workspace_id = 'd8a5abe0-9eed-406d-ab46-343bc57ddbe5'

        lakehouse = fc.create_lakehouse(workspace_id=workspace_id, display_name="lakehouse2")
        self.assertIsNotNone(lakehouse.id)

        lakehouses = fc.list_lakehouses(workspace_id)
        lakehouse_names = [lh.display_name for lh in lakehouses]
        self.assertGreater(len(lakehouse_names), 0)
        self.assertIn("lakehouse2", lakehouse_names)

        lakehouse2 = fc.get_lakehouse(workspace_id=workspace_id, lakehouse_id=lakehouse.id)
        self.assertEqual(lakehouse.id, lakehouse2.id)

        sleep(20)
        lakehouse2 = fc.update_lakehouse(workspace_id=workspace_id, lakehouse_id=lakehouse.id, display_name="lakehouse3", return_item=True)
        self.assertEqual(lakehouse2.display_name, "lakehouse3")

        id = lakehouse2.id

        lakehouse2 = fc.get_lakehouse(workspace_id=workspace_id, lakehouse_name="lakehouse3")
        self.assertEqual(lakehouse2.id, id)

        status_code = fc.delete_lakehouse(workspace_id=workspace_id, lakehouse_id=lakehouse.id)
        self.assertEqual(status_code, 200)