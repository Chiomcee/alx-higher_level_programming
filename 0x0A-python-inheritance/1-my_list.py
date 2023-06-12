#!/usr/bin/python3
"""A module that inherits from the class list"""


class MyList(list):
    """A class that inherits from the list"""
    def print_sorted(self):
        """function that prints a sorted list"""
        print(sorted(self))
