#!/usr/bin/python3

""" class that inherit from list"""


class MyList(list):

    def print_sorted(self):
        """prints the list in ascending sort"""
        print(sorted(self))
