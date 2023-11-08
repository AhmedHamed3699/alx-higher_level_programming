#!/usr/bin/python3
"""A module for writing to a file."""


def write_file(filename="", text=""):
    """
    Write to a text file (UTF8).

    Returns the number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        number_of_characters = file.write(text)
        return number_of_characters
