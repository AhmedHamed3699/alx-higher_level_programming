#!/usr/bin/python3
"""Base Module."""


class Base:
    """Base Class."""

    __nb_objects = 0

    def __init__(self, id_num=None):
        """Construct a Base object."""
        if id_num:
            self.id = id_num
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
