#!/usr/bin/python3
"""A module for studen class."""


class Student:
    """Class for student."""

    def __init__(self, first_name, last_name, age):
        """Construct a new object."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert class to json dictionary."""
        my_dict = self.__dict__
        if isinstance(attrs, list):
            new_dict = {}
            for attr in attrs:
                if not isinstance(attr, str):
                    return my_dict
                if my_dict.get(attr):
                    new_dict[attr] = my_dict[attr]
            del my_dict
            my_dict = new_dict
        return my_dict
