#!/usr/bin/python3
"""Module defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, mode='r+', encoding='utf-8') as f:
        lines = f.readlines()  # Read all lines of the file
        f.seek(0)  # Reset the file pointer to the beginning of the file
        for line in lines:
            f.write(line)  # Write the line to the file
            if search_string in line:
                f.write(new_string)
            f.truncate()
