#!/usr/bin/python3
"""This modules defines a function that reads a text file"""


def read_file(filename=""):
    """Reads a text file and output its contents to stdout"""

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
