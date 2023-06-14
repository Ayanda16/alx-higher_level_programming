#!/usr/bin/python3
"""Write to a file"""


def write_file(filename=="", text=""):
    """writes a string to a text file and returns a number of
    chracters written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
