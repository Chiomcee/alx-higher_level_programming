#!/usr/bin/python3
"""Module that defines a file-appending function"""


def append_write(filename="", text=""):
    """Append a string at the end of a UFT-8 text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
