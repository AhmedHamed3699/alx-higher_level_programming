#!/usr/bin/python3
"""Base Module."""
import json
from pathlib import Path


class Base:
    """Base Class."""

    __nb_objects = 0

    def __init__(self, id_num=None):
        """Construct a Base object."""
        if id_num:
            self.id = id_num
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert list_dictionaries to json."""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save objects to file."""
        saved_list = []
        for obj in list_objs:
            saved_list.append(obj.to_dictionary())
        with open(f'{cls.__name__}.json', 'w', encoding='utf-8') as file:
            file.write(cls.to_json_string(saved_list))

    @staticmethod
    def from_json_string(json_string):
        """Convert json string to list of dictionaries."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance."""
        from models.rectangle import Rectangle
        from models.square import Square
        inst = None
        if cls is Rectangle:
            inst = Rectangle(1, 1)
        elif cls is Square:
            inst = Square(1)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """Load objects from file."""
        file_name = f'{cls.__name__}.json'
        file_path = Path(file_name)
        if not file_path.is_file():
            return []
        obj_list = []
        json_dict = ""
        with open(file_name, 'r', encoding='utf-8') as file:
            json_dict = file.read()
        obj_list_dict = cls.from_json_string(json_dict)
        for obj_dict in obj_list_dict:
            new_obj = cls.create(**obj_dict)
            obj_list.append(new_obj)
        return obj_list
