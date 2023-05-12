#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    argv = sys.argv[1:]
    result = 0
    for arg in argv:
        result += int(arg)
    print(result)
