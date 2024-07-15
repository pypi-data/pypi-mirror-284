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
    
    def test_list_other_items(self):

        fc = self.fc

        workspace_id = 'd8a5abe0-9eed-406d-ab46-343bc57ddbe5'

        list_dashboards = fc.list_dashboards(workspace_id)
        dashboard_names = [dashboard.display_name for dashboard in list_dashboards]
        self.assertGreater(len(list_dashboards), 0)
        self.assertIn("dashboard1", dashboard_names)

        list_datamarts = fc.list_datamarts(workspace_id)
        datamart_names = [datamart.display_name for datamart in list_datamarts]
        self.assertGreater(len(list_datamarts), 0)
        self.assertIn("datamart1", datamart_names)

        list_sql_endpoints = fc.list_sql_endpoints(workspace_id)
        sqlendpoint_names = [sqlendpoint.display_name for sqlendpoint in list_sql_endpoints]
        self.assertGreater(len(list_sql_endpoints), 0)
        self.assertIn("sqlendpointlakehouse", sqlendpoint_names)

        # list_mirrored_warehouses = fc.list_mirrored_warehouses(self.workspace_id)
        # self.assertGreater(len(list_mirrored_warehouses), 0)

        # list_paginated_reports = fc.list_paginated_reports(self.workspace_id)
        # self.assertGreater(len(list_paginated_reports), 0)