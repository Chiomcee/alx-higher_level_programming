#!/usr/bin/python3
"""Module that defines a JSON_to_object function"""
import json


def from_json_string(my_str):
    """returns an object represented by JSON string"""
    return json.loads(my_str)
