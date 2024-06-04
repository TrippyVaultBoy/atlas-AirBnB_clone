import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_city_id(self):
        self.place = Place()
        self.assertEqual(self.place.city_id, "")
        self.place.city_id = "TUL"
        self.assertEqual(self.place.city_id, "TUL")

    def test_user_id(self):
        self.place = Place()
        self.assertEqual(self.place.user_id, "")
        self.place.user_id = "121212"
        self.assertEqual(self.place.user_id, "121212")

    def test_name(self):
        self.place = Place()
        self.assertEqual(self.place.name, "")
        self.place.name = "Tulsa"
        self.assertEqual(self.place.name, "Tulsa")

    def test_description(self):
        self.place = Place()
        self.assertEqual(self.place.description, "")
        self.place.description = "A nice place."
        self.assertEqual(self.description, "A nice place.")

    def test_number_rooms(self):
        self.place = Place()
        self.assertEqual(self.number_rooms, 0)
        self.place.number_rooms = 3
        self.assertEqual(self.place.number_rooms, 3)

    def test_number_bathrooms(self):
        self.place = Place()
        self.assertEqual(self.place.number_bathrooms, 0)
        self.place.number_bathrooms = 4
        self.assertEqual(self.place.number_bathrooms, 4)

    def test_max_guest(self):
        self.place = Place()
        self.assertEqual(self.place.max_guest, 0)
        self.place.max_guest = 7
        self.assertEqual(self.place.max_guest, 7)

    def test_price_by_night(self):
        self.place = Place()
        self.assertEqual(self.place.price_by_night, 0)
        self.place.price_by_night = 250
        self.assertEqual(self.place.price_by_night, 250)

    def test_latitude(self):
        self.place = Place()
        self.assertEqual(self.place.latitude, 0.0)
        self.place.latitude = 1.1
        self.assertEqual(self.place.latitude, 1.1)

    def test_longitude(self):
        self.place = Place()
        self.assertEqual(self.place.longitude, 0.0)
        self.place.longitude = 2.2
        self.assertEqual(self.place.longitude, 2.2)

    def test_amenity_ids(self):
        self.place = Place()
        self.assertEqual(self.place.amenity_ids, [])
        self.place.amenity_ids = [bar, pool, hottub]
        self.assertEqual(self.place.amenity_ids, [bar, pool, hottub])
