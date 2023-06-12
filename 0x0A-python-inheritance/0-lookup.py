#!/usr/bin/python3
"""
    A module that returns the list of available attributes
    and methods of an object
"""


def lookup(obj):
        """A function that retrieves  all attributes and method of an object"""
        return dir(obj)
