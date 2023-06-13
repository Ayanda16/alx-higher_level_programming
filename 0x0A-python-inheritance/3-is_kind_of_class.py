#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """returns true if the object is an instance of, or an instance
    of a class that inherited from the specified class, otherwise false"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
