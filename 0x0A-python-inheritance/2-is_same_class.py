#!/usr/bin/python3
"""verifies if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """takes two arguments,  uses type() to get class of the
    object and compares with specified class

    Returns:
        if the classes match, it returns True.
        otherwisw - False.
    """
    return (type(obj) is a_class)
