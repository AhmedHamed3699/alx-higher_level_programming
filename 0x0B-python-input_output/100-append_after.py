#!/usr/bin/python3
"""A module for dealing with files and strings."""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text to a file.
    after each line containing a specific string
    """
    text = ''
    with open(filename) as file:
        line = file.readline()
        while line != '':
            text += line
            if line.find(search_string) != -1:
                text += new_string
            line = file.readline()
    with open(filename, 'w') as file:
        file.write(text)
