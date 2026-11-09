import unittest

from pricing import apply_discount


class TestPricing(unittest.TestCase):
    def test_ten_percent(self):
        self.assertEqual(apply_discount(100, 10), 90)

    def test_quarter_off(self):
        self.assertEqual(apply_discount(200, 25), 150)

    def test_non_round_price_ten_percent(self):
        self.assertEqual(apply_discount(19.99, 10), 17.99)

    def test_non_round_price_fifteen_percent(self):
        self.assertEqual(apply_discount(49.99, 15), 42.49)

    def test_non_round_price_small(self):
        self.assertEqual(apply_discount(9.99, 10), 8.99)


if __name__ == "__main__":
    unittest.main()
