#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list_t=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list_t) == 0:
        return None
    result = list_t[0]
    i = 1
    while i < len(list_t):
        if list_t[i] > result:
            result = list_t[i]
        i += 1
    return result
