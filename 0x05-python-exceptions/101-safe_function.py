#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Executes a function safely."""
    try:
        result = fct(*args)
        return (result)
    except Exception as err:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
