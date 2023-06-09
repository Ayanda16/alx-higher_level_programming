#!/usr/bin/python3
"""integer addition"""


def add_integer(a, b=98):
    """adds two integers and returns an inter"""
    if type(a) is not (int, float):
        raise TypeError ("a must be an integer")
    if type(b) is not (int, float):
        raise TypeError ("b must be an integer")
    return(int(a) + int(b))
