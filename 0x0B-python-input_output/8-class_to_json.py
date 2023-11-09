#!/usr/bin/python3
"""A module for dealing with class and JSON."""


def class_to_json(obj):
    """Return the dictionary description of an object."""
    return obj.__dict__
