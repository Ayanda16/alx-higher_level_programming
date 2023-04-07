#!/usr/bin/python3
""" Define an area and perimeter of a rectangle"""


class Rectangle():
    """Defining a class rectangle"""
    def __init__(self, width=0, height=0):
        """ initialising a rectagle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting width properties"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting height properties"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """ return the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return((self.__width * 2) + (self.__height * 2))
