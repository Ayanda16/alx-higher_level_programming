#!/usr/bin/python3
"""create object from json file"""


def load_from_json_file(filename):
    """create an object from json file"""
    with open(filename) as f:
        return json.load(f)
