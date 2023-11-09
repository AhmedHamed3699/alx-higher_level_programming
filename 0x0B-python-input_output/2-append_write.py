#!/usr/bin/python3
"""A module for appending to a file."""


def append_write(filename="", text=""):
    """
    Append to a text file (UTF8).

    Returns the number of characters written.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        number_of_characters = file.write(text)
        return number_of_characters
