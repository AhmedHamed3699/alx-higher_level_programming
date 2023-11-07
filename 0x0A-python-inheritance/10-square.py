#!/usr/bin/python3
"""A module for implementing rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class, derived from rectangle."""

    def __init__(self, size):
        """Construct Square."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Get Area."""
        return (self.__size) ** 2
