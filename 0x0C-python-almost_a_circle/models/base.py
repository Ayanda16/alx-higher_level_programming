#!/usr/bin/python3
"""class Base that will manage id attribute in all future classes"""


class Base:
    """ Base class of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialise class Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
