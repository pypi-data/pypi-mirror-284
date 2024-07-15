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

    
    def test_ml_models(self):

        fc = self.fc
        workspace_id = 'd8a5abe0-9eed-406d-ab46-343bc57ddbe5'
        datetime_str = datetime.now().strftime("%Y%m%d%H%M%S")
        model_name = "mlm" + datetime_str

        ml_model = fc.create_ml_model(workspace_id, display_name=model_name)
        self.assertEqual(ml_model.display_name, model_name)
        
        ml_models = fc.list_ml_models(workspace_id)
        ml_model_names = [ml.display_name for ml in ml_models]
        self.assertGreater(len(ml_models), 0)
        self.assertIn(model_name, ml_model_names)

        mlm = fc.get_ml_model(workspace_id, ml_model_name=model_name)
        self.assertIsNotNone(mlm.id)
        self.assertEqual(mlm.display_name, model_name)

        mlm2 = fc.update_ml_model(workspace_id=workspace_id,ml_model_id= mlm.id,  description=model_name, return_item=True)

        mlm = fc.get_ml_model(workspace_id, ml_model_id=mlm.id)
        self.assertEqual(mlm.description, model_name)
        self.assertEqual(mlm.id, mlm2.id)

        status_code = fc.delete_ml_model(workspace_id, mlm.id)
        self.assertEqual(status_code, 200)