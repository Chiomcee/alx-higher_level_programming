#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # sort the keys in aplhabetical order
    sorted_keys = sorted(a_dictionary.keys())

    # Iterate over the sorted keys and print each key_value pair
    for key in sorted_keys:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
