"""
test class for python_app.py
"""
from unittest import TestCase
from pyhton_app import result

class TestingResultFunction(TestCase):
    """
    tests for the exercise
    """
    def test_always_passes(self):
        """
        uses example from the exercise
        """
        self.assertEqual(result("test_input.txt"), 2028)
