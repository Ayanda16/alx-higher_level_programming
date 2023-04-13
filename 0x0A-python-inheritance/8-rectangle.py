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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """class Rectangle inherited from class BaseGeometry"""

    def __init__(self, width, height):
        """ initialisation of class Rectangle"""
        
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
