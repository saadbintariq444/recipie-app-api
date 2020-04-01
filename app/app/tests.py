from django.test import TestCase

from app.calc import add

from app.calc import subtr

class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that values are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtr_numbers(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(subtr(5, 11), 6)
