#!/usr/bin/python3
# 0-square.py by Chioma Igwe
"""Defines a square"""


class Square:
    """Describes a class Square"""

    def __init__(self, size=0):
        """Initializes this square class
        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
