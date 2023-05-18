#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # Create a new empty dictionary
    new_dictionary = {}
    # iterates over the key-value pairs in the a_dictionary using item() method
    for key, value in a_dictionary.items():
        new_dictionary[key] = value * 2
    return new_dictionary
