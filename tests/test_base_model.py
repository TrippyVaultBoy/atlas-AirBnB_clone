#!/usr/bin/python3
import unittest
from base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_save(self):
        model = BaseModel()
        