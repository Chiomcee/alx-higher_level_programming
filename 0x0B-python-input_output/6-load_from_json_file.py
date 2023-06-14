#!/uisr/bin/python3
"""Module that converts a JSON file to python object"""
import json


def load_from_json_file(filename):
    """function that creates an object from JSON file"""
    with open(filename) as f:
        return json.load(f)
