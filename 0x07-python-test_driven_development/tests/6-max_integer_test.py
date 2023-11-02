#!/usr/bin/python3
"""Unittest for max_integer([..])."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This class is used as a unit test."""

    def test_values(self):
        """Test different value inputs."""
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([5, 5, 5.0000000001]), 5.0000000001)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([-5, -3, -9]), -3)
