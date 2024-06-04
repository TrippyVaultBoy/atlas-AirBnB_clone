import unittest
from models.user import User
"""
Includes the TestUser class
"""

class TestUser(unittest.TestCase):
    """
    Class tests the user class
    """

    def test_email(self):
        self.user = User()
        self.assertEqual(self.user.email, "")
        self.user.email = "test@example.com"
        self.assertEqual(self.user.email, "test@example.com")

    def test_password(self):
        self.user = User()
        self.assertEqual(self.user.password, "")
        self.user.password = "12345"
        self.assertEqual(self.user.password, "12345")

    def test_first_name(self):
        self.user = User()
        self.assertEqual(self.user.first_name, "")
        self.user.first_name = "John"
        self.assertEqual(self.user.first_name, "John")

    def test_last_name(self):
        self.user = User()
        self.assertEqual(self.user.last_name, "")
        self.user.last_name = "Smith"
        self.assertEqual(self.user.last_name, "Smith")
