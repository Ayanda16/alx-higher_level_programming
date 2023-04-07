#!/usr/bin/python3
"""define a rectangle"""


class Rectangle:
    """ defining class rectangle"""
    def __init__(self, width=0, height=0):
        """initialise rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve the width"""
        return self.__width

    @property
    def height(self):
        """retrieve the height of the triangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """set width properties"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """set height properties"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the rectangle parametere"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__width + self.__height)*2)

    def __str__(self):
        """string representation of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        Rectangle = []
        for i in range(self.__height):
            [Rectangle.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                Rectangle.append("\n")
        return ("".join(Rectangle))
