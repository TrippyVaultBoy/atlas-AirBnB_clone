import unittest
from models.amenity import Amenity
"""
Includes the TestAmenity class
"""

class TestAmenity(unittest.TestCase):
    """
    Class tests the Amenity class
    """

    def test_name(self):
        self.amenity = Amenity()
        self.assertEqual(self.amenity.name, "")
        self.amenity.name = "Pool & Spa"
        self.assertEqual(self.amenity.name, "Pool & Spa")