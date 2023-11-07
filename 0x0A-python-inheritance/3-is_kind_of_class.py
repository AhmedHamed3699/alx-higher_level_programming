#!/usr/bin/python3
"""A module for checking if an object is an instance of a class."""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance of, or instance of a derived class."""
    return isinstance(obj, a_class)
