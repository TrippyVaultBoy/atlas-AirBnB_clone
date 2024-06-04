import unittest
from models.city import City
"""
Includes the TestCity class
"""

class TestCity(unittest.TestCase):
    """
    Class tests the City class
    """

    def test_state_id(self):
        self.city = City()
        self.assertEqual(self.city.state_id, "")
        self.city.state_id = "OK"
        self.assertEqual(self.city.state_id, "OK")

    def test_name(self):
        self.city = City()
        self.assertEqual(self.city.name, "")
        self.city.name = "Tulsa"
        self.assertEqual(self.city.name, "Tulsa")
