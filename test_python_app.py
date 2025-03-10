"""
test class for python_app.py
"""
from unittest import TestCase
from pyhton_app import result
from guide_app import result as guide_app_result

class TestingResultFunction(TestCase):
    """
    tests for the exercise
    """
    def test_rest_python_app(self):
        """
        uses example from the exercise
        """
        self.assertEqual(result("test_input.txt"), 2028)

    def test_result_guide_app(self):
        """
        uses example from the exercise
        """
        self.assertEqual(guide_app_result("guide_test_input.txt"), 11)
