"""Checkout pricing helpers."""


def apply_discount(price, percent):
    """Return the price after a percent discount, rounded to 2 decimals.

    A discount of 100% or more is a full discount, so the price is 0.
    The result is never negative.
    """
    discounted = price - price * percent / 100
    return round(max(discounted, 0), 2)
