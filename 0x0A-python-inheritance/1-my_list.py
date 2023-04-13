#!/usr/bin/python3

"""define a subclass MyList from list"""


class MyList(list):
    """class MyList that iherits from superclass list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
