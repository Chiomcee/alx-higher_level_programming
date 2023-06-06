#!/usr/bin/python3
# 0-add_integer.py

def add_integer(a, b=98):
    """
    Return the integer addition of a and b.
    Float arguments are typecasted to ints before addition is performed.

    Args:
        a: An integer or float.
        b: An integer or float. Default value is 98.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.

    Returns:
        The integer addition of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")
    return int(a) + int(b)
