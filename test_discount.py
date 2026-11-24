import unittest
from discount import apply_discount


class TestDiscount(unittest.TestCase):

    def test_10_percent_discount(self):
        self.assertEqual(apply_discount(100, 10), 90)

    def test_50_percent_discount(self):
        self.assertEqual(apply_discount(200, 50), 100)

    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            apply_discount(100, 150)


if __name__ == "__main__":
    unittest.main()