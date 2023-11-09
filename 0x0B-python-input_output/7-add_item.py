#!/usr/bin/python3
"""A module for JSON representation."""
import json
import sys
from pathlib import Path
save_to_file = __import__("5-save_to_json_file").save_to_json_file
load_from_file = __import__("6-load_from_json_file").load_from_json_file


if __name__ == '__main__':
    args = sys.argv
    Path("add_item.json").touch()
    try:
        my_list = load_from_file("add_item.json")
    except json.decoder.JSONDecodeError:
        my_list = []
    for index in range(1, len(args)):
        my_list.append(args[index])
    save_to_file(my_list, "add_item.json")
