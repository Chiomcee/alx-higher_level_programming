#!/usr/bin/python3
"""Module that defines a python class to JSON function"""


def class_to_json(obj):
    """returns the dict. representation of obj. instance variable"""
    return obj.__dict__
