#!/usr/bin/python3

"""write to a file"""


def write_file(filename="", text=""):
    """writes a string to a txt file and returns the number of chars written"""

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
