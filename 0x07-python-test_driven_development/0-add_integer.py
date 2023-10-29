#!/usr/bin/python3
"""A module for adding numbers."""


def add_integer(a, b=98):
    """Add two number a, b and return result."""
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
