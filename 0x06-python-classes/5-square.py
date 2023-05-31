#!/usr/bin/python3

class Square:
    """
    Represents a square.
    """

    def __init__(self, size):
        """
        Initializes a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """
        Gets/sets the current size of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        Returns the current area of the square.
        """
        return self.size * self.size

    def my_print(self):
        """
        Prints the square with the # character.
        """
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print("")
