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

    def test_semantic_models(self):
                    
        fc = self.fc
        workspace_id = 'd8a5abe0-9eed-406d-ab46-343bc57ddbe5'

        semantic_model_name = "semanticmodel1234"

        semantic_model_w_content = fc.get_semantic_model(workspace_id, semantic_model_name="Table")

        definition = fc.get_semantic_model_definition(workspace_id, semantic_model_w_content.id)

        self.assertIsNotNone(definition)
        self.assertIn("definition", definition)
        definition = definition["definition"]
        semantic_model = fc.create_semantic_model(workspace_id, display_name=semantic_model_name, definition=definition)
        fc.update_semantic_model_definition(workspace_id, semantic_model.id, definition=definition)
        semantic_model = fc.get_semantic_model(workspace_id, semantic_model_id=semantic_model.id)
        self.assertEqual(semantic_model.display_name, semantic_model_name)
        self.assertIsNotNone(semantic_model.definition)
        
        semantic_models = fc.list_semantic_models(workspace_id)
        semantic_model_names = [sm.display_name for sm in semantic_models]
        self.assertGreater(len(semantic_models), 0)
        self.assertIn(semantic_model_name, semantic_model_names)

        sm = fc.get_semantic_model(workspace_id, semantic_model_name=semantic_model_name)
        self.assertIsNotNone(sm.id)
        self.assertEqual(sm.display_name, semantic_model_name)

        status_code = fc.delete_semantic_model(workspace_id, sm.id)
        self.assertEqual(status_code, 200)