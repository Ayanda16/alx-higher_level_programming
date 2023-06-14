#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """function that reads a text file and prints it to STDOUT"""
    with open(filename, encoding='UTF-8') as f:
        print(f.read(), end="")
