#!/usr/bin/python3
""" class to JSON"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    for JSON serialisation of an object"""
    return obj.__dict__
