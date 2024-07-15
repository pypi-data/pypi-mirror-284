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


    def test_warehouses(self):

        fc = self.fc
        workspace_id = 'd8a5abe0-9eed-406d-ab46-343bc57ddbe5'

        datetime_str = datetime.now().strftime("%Y%m%d%H%M%S")
        warehouse1 = f"wh{datetime_str}"
        warehouse = fc.create_warehouse(workspace_id, display_name=warehouse1)
        self.assertIsNotNone(warehouse.id)

        warehouses = fc.list_warehouses(workspace_id)
        warehouse_names = [wh.display_name for wh in warehouses]
        self.assertGreater(len(warehouses), 0)
        self.assertIn(warehouse1, warehouse_names)

        warehouse = fc.get_warehouse(workspace_id, warehouse_name=warehouse1)
        self.assertIsNotNone(warehouse.id)
        self.assertEqual(warehouse.display_name, warehouse1)

        warehouse2 = fc.update_warehouse(workspace_id, warehouse.id, display_name=f"{warehouse1}2", return_item=True)
        warehouse = fc.get_warehouse(workspace_id, warehouse_id=warehouse.id)
        self.assertEqual(warehouse.display_name, f"{warehouse1}2")
        self.assertEqual(warehouse.id, warehouse2.id)

        status_code = fc.delete_warehouse(workspace_id, warehouse.id)
        self.assertEqual(status_code, 200)


if __name__ == "__main__":
    unittest.main()