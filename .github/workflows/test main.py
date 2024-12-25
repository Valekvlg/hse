# test_main.py
import unittest
from main import calculate_square

class TestCalculateSquare(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(calculate_square(4), 16)

    def test_negative_number(self):
        self.assertEqual(calculate_square(-3), 9)

    def test_zero(self):
        self.assertEqual(calculate_square(0), 0)

if __name__ == "__main__":
    unittest.main()
