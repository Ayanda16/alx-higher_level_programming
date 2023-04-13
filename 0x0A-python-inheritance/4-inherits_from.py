#!/usr/bin/python3
"""function that returns true if the object is an instance of a class that
   inherited from the specified class, otherwise false"""


def inherits_from(obj, a_class):
    """returns true if the obj is an instance of a class that inherited
        from a_class"""
    if issubclass(type(obj), a_class):
        return True
    return False
