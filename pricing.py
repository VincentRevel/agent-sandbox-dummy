"""Checkout pricing helpers."""


def apply_discount(price, percent):
    """Return the price after a percent discount, rounded to 2 decimals."""
    return round(price - price * percent // 100, 2)
