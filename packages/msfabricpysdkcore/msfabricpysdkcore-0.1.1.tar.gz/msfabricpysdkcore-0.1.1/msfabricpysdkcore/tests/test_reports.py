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


    def test_reports(self):
                
        fc = self.fc
        workspace_id = 'd8a5abe0-9eed-406d-ab46-343bc57ddbe5'

        report_name = "report1234"

        report_w_content = fc.get_report(workspace_id, report_name="HelloWorldReport")

        definition = fc.get_report_definition(workspace_id, report_w_content.id)
        
        self.assertIsNotNone(definition)
        self.assertIn("definition", definition)
        definition = definition["definition"]

        report = fc.create_report(workspace_id, display_name=report_name, definition=definition)
        fc.update_report_definition(workspace_id, report.id, definition=definition)
        report = fc.get_report(workspace_id, report_id=report.id)
        self.assertEqual(report.display_name, report_name)
        self.assertIsNotNone(report.definition)
        
        reports = fc.list_reports(workspace_id)
        report_names = [r.display_name for r in reports]
        self.assertGreater(len(reports), 0)
        self.assertIn(report_name, report_names)

        r = fc.get_report(workspace_id, report_name=report_name)
        self.assertIsNotNone(r.id)
        self.assertEqual(r.display_name, report_name)

        status_code = fc.delete_report(workspace_id, r.id)
        self.assertEqual(status_code, 200)