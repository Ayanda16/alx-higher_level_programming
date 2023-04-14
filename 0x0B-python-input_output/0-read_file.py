#!/usr/bin/python3

""" define a fuction that Reads afile """


def read_file(filename=""):
    """ reads a text file and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
