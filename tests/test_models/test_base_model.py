import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        self.base_model = BaseModel()
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)
        self.assertEqual(self.base_model.created_at, self.base_model.updated_at)

    def test_init_kwargs(self):
        
        kwargs = {
            "id": str(uuid.uuid4()),
            "created_at": "2024-06-03T00:00:00.000000",
            "updated_at": "2024-06-03T00:00:00.000000",
            "name": "Test" 
        }
        self.base_model = BaseModel(**kwargs)
        self.assertEqual(self.base_model.id, kwargs["id"])
        self.assertEqual(self.base_model.created_at, datetime.strptime(kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(self.base_model.updated_at, datetime.strptime(kwargs["updated_at"], '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(self.base_model.name, "Test")

    def test_str(self):
        self.base_model = BaseModel()
        correct_output = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), correct_output)
