#!/usr/bin/python3
"""This module defines a class MyInt which inherits from int"""


class MyInt(int):
    """This class represents a rebel integer"""

    def __eq__(self, other):
        """Overrides the == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides the != operator"""
        return super().__eq__(other)
