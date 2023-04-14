#!/usr/bin/python3

""" fuction that returns the JSON representation of an object"""


import json


def to_json_string(my_obj):
    """ return json representation of an object"""
    return json.dumps(my_obj)
