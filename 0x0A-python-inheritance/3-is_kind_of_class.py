#!/usr/bin/python3

"""returns true if the object is an instant of, or if the object is an
    instance of a class that inherited from the specified class"""


def is_kind_of_class(obj, a_class):
    """returns true/false based on wheather the object is of given type"""
    if not isinstance(obj, a_class):
        return False
    else:
        True
