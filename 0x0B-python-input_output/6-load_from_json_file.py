#!/usr/bin/python3
"""A module for JSON representation."""
import json


def load_from_json_file(filename):
    """Create an Object from a “JSON file”."""
    with open(filename, 'r', encoding='utf-8') as file:
        string_json = file.read()
        return json.loads(string_json)
