#!/usr/bin/python3
def safe_print_integer_err(value):
    """Print an integer value and return
    True if value is an integer, otherwise
    return False and print error message to stderr"""
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
