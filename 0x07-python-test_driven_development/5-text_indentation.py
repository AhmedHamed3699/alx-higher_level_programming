#!/usr/bin/python3
"""A module dealing with parsing a text."""


def text_indentation(text=''):
    """Print text with 2 new lines after each of these characters:(. ? :)."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = False
    spaces = ''
    for char in text:
        if char in ('.', '?', ':'):
            print(char + '\n')
            spaces = ''
            flag = True
        elif char == ' ':
            spaces += ' '
            continue
        else:
            if flag:
                spaces = ''
                flag = False
            print(spaces + char, end='')
            spaces = ''
