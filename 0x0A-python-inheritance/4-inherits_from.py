#!/usr/bin/python3
"""A module for checking if an object is an instance of a subclass."""


def inherits_from(obj, a_class):
    """Check if object is an instance of a derived class."""
    return isinstance(obj, a_class) and (not type(obj) is a_class)
