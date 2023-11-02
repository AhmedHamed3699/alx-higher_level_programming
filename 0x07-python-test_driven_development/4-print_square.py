#!/usr/bin/python3
"""A Module for printing a square and testing it."""


def print_square(size=0):
    """Print a square with side length is size."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        for _ in range(size):
            print("#", end='')
        print()
