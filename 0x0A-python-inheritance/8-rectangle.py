#!/usr/bin/python3
"""A module for implementing rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class, derived from BaseGeometry."""

    def __init__(self, width, height):
        """Construct Rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
