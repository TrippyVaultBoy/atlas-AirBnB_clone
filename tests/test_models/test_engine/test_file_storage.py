from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import unittest
from unittest.mock import patch
import json
import os


class TestFileStorage(unittest.TestCase):
    def test_file_path(self):
        self.storage = FileStorage()
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_all(self):
        self.storage = FileStorage()
        test_dict = self.storage.all()
        self.assertEqual(type(test_dict), dict)
        self.assertIs(test_dict, self.storage._FileStorage__objects)

    def test_new(self):
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.storage.new(self.obj)
        key = f"BaseModel.{self.obj.id}"
        self.assertIn(key, self.storage._FileStorage__objects)
        self.assertEqual(self.storage._FileStorage__objects[key], self.obj)

    def test_save(self):
        pass

    def test_reload(self):
        pass
