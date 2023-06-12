#!/usr/bin/python3
"""Defines a base geometry class"""


class BaseGeometry:
    """Represents a base geometry"""

    def area(self):
        """method yet to be implemented"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validates avalue as integer"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
