#!/usr/bin/python3
"""checks an inherited instance of a class object."""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherited from a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a class that inherited from a_class,
        otherwise False.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
