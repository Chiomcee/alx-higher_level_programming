#!/usr/bin/python3
"""Module that creates a UTF-8 txt file and write a string to it"""


def write_file(filename="", text=""):
    """creates a text file and write a string to it."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
