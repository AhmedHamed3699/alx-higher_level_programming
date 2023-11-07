#!/usr/bin/python3
"""A module for a rebel int class."""


class MyInt(int):
    """Class MyInt, derived from int."""

    def __eq__(self, other):
        """Check equality of two integers."""
        if not isinstance(other, int):
            return False
        if self.real == other.real:
            return False
        return True

    def __ne__(self, other):
        """Check inequality of two integers."""
        if not isinstance(other, int):
            return False
        if self.real == other.real:
            return True
        return False
