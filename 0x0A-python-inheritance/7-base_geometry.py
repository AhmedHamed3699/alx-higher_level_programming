#!/usr/bin/python3
"""A module for implementing geometry."""


class BaseGeometry:
    """Base class for geometry related classes."""

    def area(self):
        """Get Area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value."""
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
