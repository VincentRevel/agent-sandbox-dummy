import unittest

from pricing import apply_discount


class TestPricing(unittest.TestCase):
    def test_ten_percent(self):
        self.assertEqual(apply_discount(100, 10), 90)

    def test_quarter_off(self):
        self.assertEqual(apply_discount(200, 25), 150)


if __name__ == "__main__":
    unittest.main()
