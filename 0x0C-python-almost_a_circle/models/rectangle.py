#!/usr/bin/python3
""" Class rectangle that inherits from class Base"""
from models.base import Base


class Rectangle(Base):
    """defining class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialising class rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of rectagle"""
        return (self.__width * self.__height)

    def display(self):
        """prints in stdout the rectangle with character #"""
        if self.__width == 0 or self.__height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.__height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """return string representation of rectangle"""
        r = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y,
                                                   self.__width, self.__height)
        return r
