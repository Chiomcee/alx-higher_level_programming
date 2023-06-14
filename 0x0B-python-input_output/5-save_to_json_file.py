#!/usr/bin/python3
"""Module that defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """write the object to the file in JSON format"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)