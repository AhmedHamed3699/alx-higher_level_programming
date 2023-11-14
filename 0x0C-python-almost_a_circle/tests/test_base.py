#!/usr/bin/python3
"""Test Module."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """A class from testing Base class."""

    def test_id(self):
        """Test dealing with id of new objects."""
        b = Base()
        self.assertEqual(b.id, 1)
