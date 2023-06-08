#!/usr/bin/python3
"""defines a class rectangle"""


class Rectangle:
    """represents a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialisaton of rectangle
           width: width of the rectangle
           height: height of the rectangle"""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
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
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """"magic method to return rectangle with # representation"""
        print_symbol = str(self.print_symbol)
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = ""
        for i in range(self.height - 1):
            rectangle += print_symbol * self.width + "\n"
        rectangle += print_symbol * self.width
        return (rectangle)

    def __repr__(self):
        """return a string representation of class rectangle"""
        rectangle = "Rectangle({}, {})".format(self.__width, self.__height)
        return rectangle

    def __del__(self):
        """instance method to detect instance deletion"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
