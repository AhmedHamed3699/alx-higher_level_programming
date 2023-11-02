#!/usr/bin/python3
"""A class Square that defines a square."""


class Square:
    """A Square class."""

    def __init__(self, size=0):
        """Construct the class."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size