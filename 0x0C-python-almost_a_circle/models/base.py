#!/usr/bin/python3
"""This is a module with a class that serve as a base for other classes"""


import os
import json
import csv
import turtle

class Base:
    """A class representing base of all classes created"""

    __nb_objects = 0

    def __init__(self, id=None):
        """function class constructor""" 
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects