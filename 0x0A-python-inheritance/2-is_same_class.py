#!/usr/bin/python3
"""fuction that returns true if the object is exactly an instance
        of the specified class, otherwise false"""


def is_same_class(obj, a_class):
    """fuction that returns true if the object is exactly an instance
    of the specified class, otherwise false"""
    if type(obj) == a_class:
        return True
    else:
        False
