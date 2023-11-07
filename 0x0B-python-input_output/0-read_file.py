#!/usr/bin/python3
"""A module for reading from a file."""


def read_file(filename=""):
    """Read a text file (UTF8) and prints it to stdout."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
