#!/usr/bin/python3
""" Module that defines a Square class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class that defines a square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Method that returns the string representation of the square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ Method that returns the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ Method that sets the size of the square """
        self.width = value
        self.height = value
