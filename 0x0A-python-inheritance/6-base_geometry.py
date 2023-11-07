#!/usr/bin/python3
"""A module for implementing geometry."""


class BaseGeometry:
    """Base class for geometry related classes."""

    def area(self):
        """Get Area."""
        raise Exception("area() is not implemented")
