#!/usr/bin/python3
"""
    The module contains functions that prints my name
"""


def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first name> <last name>'

    Args:
        first_name: A str representing the first name
        last_name: A str representing the last name

    Raises:
        TypeError: If first_name is not a string
        TypeError: If last_name is not a string

    Returns:
        None
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name}{last_name}")
