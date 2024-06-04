import unittest
from models.state import State
"""
Includes the TestState class
"""

class TestState(unittest.TestCase):
    """
    Class tests the State class
    """

    def test_name(self):
        self.state = State()
        self.assertEqual(self.state.name, "")
        self.state.name = "MI"
        self.assertEqual(self.state.name, "MI")