#!/usr/bin/python3
"""A module for adding new attributes."""


def add_attribute(obj, key, value):
    """Add attribute to obj."""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
