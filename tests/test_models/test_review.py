import unittest
from models.review import Review
"""
Includes the TestReview class
"""

class TestReview(unittest.TestCase):
    """
    Class tests the Review class
    """

    def test_place_id(self):
        self.review = Review()
        self.assertEqual(self.review.place_id, "")
        self.review.place_id = "1234567890"
        self.assertEqual(self.review.place_id, "1234567890")
    
    def test_user_id(self):
        self.review = Review()
        self.assertEqual(self.review.user_id, "")
        self.review.user_id = "9876543210"
        self.assertEqual(self.review.user_id, "9876543210")
    
    def test_text(self):
        self.review = Review()
        self.assertEqual(self.review.text, "")
        self.review.text = "Great place Highly recommended."
        self.assertEqual(self.review.text, "Great place Highly recommended.")