import unittest

from pricing import apply_discount


class TestDiscountOver100(unittest.TestCase):
    def test_percent_over_100_raises_value_error(self):
        with self.assertRaises(ValueError):
            apply_discount(100, 150)


if __name__ == "__main__":
    unittest.main()
