#!/usr/bin/python3
"""checks if object is an instance of a class
or inherited instance of a class
"""


def is_kind_of_class(obj, a_class):
    """returns true if object is an instance of a class
    or a class that inherited from the specified class
    """
    return (isinstance(obj, a_class))
