#!/usr/bin/python3
"""Module that dds all args to a python list
    then save to a file.
"""

import json
import sys
from os import path

def save_to_json_file(my_obj, filename):
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)

def load_from_json_file(filename):
    if path.exists(filename):
        with open(filename, mode='r', encoding='utf-8') as file:
            return json.load(file)
    return []

if __name__ == "__main__":
    arguments = sys.argv[1:]
    filename = "add_item.json"

    my_list = load_from_json_file(filename)
    my_list.extend(arguments)

    save_to_json_file(my_list, filename)
