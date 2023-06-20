#!/usr/bin/python3
"""This is a module with a class that serve as a base for other classes"""

import json


class Base:
    """A class representing base of all classes created"""

    __nb_objects = 0

    def __init__(self, id=None):
        """function class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method that writes the JSON string representation
        of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_dicts))
