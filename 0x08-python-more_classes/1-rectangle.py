#!/usr/bin/python3
"""defines a class rectangle"""


class Rectangle:
    """represents a rectangle"""

    def __init__(self, width=0, height=0):
        """initialisaton of rectangle
           width: width of the rectangle
           height: height of the rectangle"""

    @property
    def width(self):
        """get width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        "get the heght of the rectangle"
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
