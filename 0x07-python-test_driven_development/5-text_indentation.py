#!/usr/bin/python3
"""A module dealing with parsing a text."""


def text_indentation(text=''):
    """Print text with 2 new lines after each of these characters:(. ? :)."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = False
    for char in text:
        if char in ('.', '?', ':'):
            print(char + '\n')
            flag = True
        elif char == ' ' and flag:
            flag = False
            continue
        else:
            flag = False
            print(char, end='')
