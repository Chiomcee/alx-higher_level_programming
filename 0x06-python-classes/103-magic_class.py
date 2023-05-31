#!/usr/bin/python3
"""Defines a MagicClass"""
import math


class MagicClass:
    """Represents a circle"""

    def __init__(self, radius):
        """Initiazes a MagicClass"""

        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Returns area of the MagicClass"""
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """Returns circumference of the MaggicClass"""
        return 2 * math.pi * self.__radius
