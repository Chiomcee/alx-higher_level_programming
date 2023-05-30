#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Takes a size parameter
    the size is stored in a private instance attribute
    '__size' using the doube underscore prefix"""

    def __init__(self, size):
        self.__size = size
