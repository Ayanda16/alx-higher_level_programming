#!/usr/bin/python3
"""define a rectangle"""


class Rectangle:
    """ defining class rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialise rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """" returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new rectangle instance with
           width == height == size"""
        return (cls(size, size))

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
            [Rectangle.append(str(self.print_symbol)) for j in
                range(self.__width)]
            if i != self.__height - 1:
                Rectangle.append("\n")
        return ("".join(Rectangle))

    def __repr__(self):
        """create a representation"""
        new_rectangle = "{}({}, {})".format(self.__class__.__name__,
                                            self.__width, self.__height)
        return (new_rectangle)

    def __del__(self):
        """detect instance deletion"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
