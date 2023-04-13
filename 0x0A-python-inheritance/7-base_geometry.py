#!/usr/bin/python3

"""Integer validator"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public instance method that validates value to be an int type"""

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
