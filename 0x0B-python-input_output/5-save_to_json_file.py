#!/usr/bin/python3
"""A module for JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """Write an Object to a text file, using a JSON representation."""
    with open(filename, 'w', encoding='utf-8') as file:
        json_repr = json.dumps(my_obj)
        file.write(json_repr)
