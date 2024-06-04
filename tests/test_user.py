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
        u = User()
        self.assertEqual(self.user.email, "")
        self.user.email = "test@example.com"
        self.assertEqual(self.user.email, "test@example.com")