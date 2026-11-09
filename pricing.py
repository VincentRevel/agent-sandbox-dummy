"""Checkout pricing helpers."""


def apply_discount(price, percent):
    """Return the price after a percent discount, rounded to 2 decimals."""
    if percent > 100:
        raise ValueError("percent must not exceed 100")
    return round(price - price * percent / 100, 2)
