#!/usr/bin/python3
"""Define a class BaseGeometry"""


class BaseGeometry:
    """class Baseeometry"""

    def area(self):
        """puplic instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validades value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
