#!/usr/bin/python3

"""
This module contain a function that prints a square
"""

def print_square(size):
    """
    This function prints a square with the character #
    
    Args:
        size (int): represents the length of the square
    
    Raises:
        TypeError: If size is not an integer
        TypeError: If size is a float and less than zero
        ValueError: If size is less than zero
    """
    
    # Check if size is not an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    # Check if size is less than zero
    elif size < 0:
        raise ValueError("size must be >= 0")
    # Check if size is a float and less than zero
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    # Print the square
    for n in range(0, size):
        for m in range(size):
            print("#", end="")
        print("")
