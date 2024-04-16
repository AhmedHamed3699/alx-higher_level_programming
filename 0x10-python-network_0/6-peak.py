#!/usr/bin/python3
"""A Technical interview preparation question."""


def find_peak(list_of_integers):
    """Find peak value of a list of integers."""
    n = len(list_of_integers)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        x = list_of_integers[mid]
        xl = x if mid - 1 < 0 else list_of_integers[mid - 1]
        xr = x if mid + 1 >= n else list_of_integers[mid + 1]
        if x >= xl and x >= xr:
            return x
        if xl > x and xl > xr:
            right = mid - 1
        else:
            left = mid + 1
    return None
