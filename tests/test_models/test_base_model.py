import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime
from unittest.mock import patch

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

    @patch('models.storage')
    def test_save(self, mock_storage):
        self.base_model = BaseModel()
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, old_updated_at)
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)

    def test_to_dict(self):
        self.base_model = BaseModel()
        test_dict = self.base_model.to_dict()
        self.assertEqual(test_dict['__class__'], 'BaseModel')
        self.assertEqual(test_dict['id'], self.base_model.id)
        self.assertEqual(test_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(test_dict['updated_at'], self.base_model.updated_at.isoformat())
        for key in self.base_model.__dict__:
            if key not in ["created_at", "updated_at"]:
                self.assertEqual(test_dict[key], self.base_model.__dict__[key])
