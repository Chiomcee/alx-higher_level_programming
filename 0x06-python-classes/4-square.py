#!/usr/bin/python3
"""Defines a square """


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize a new square class
        Args:
            size: the size of the new square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """set the current size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Returns the curremt area of the square
        """

        return (self.__size ** 2)
