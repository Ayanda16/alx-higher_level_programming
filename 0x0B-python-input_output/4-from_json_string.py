#!/usr/bin/python3
import json
"""from JSON string to object"""


def from_json_string(my_str):
    """returns an object represented by JSON string"""
    return json.loads(my_str)
