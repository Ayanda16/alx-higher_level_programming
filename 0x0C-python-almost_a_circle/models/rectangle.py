#!/usr/bin/python3
""" Class rectangle that inherits from class Base"""
from models.base import Base


class Rectangle:
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
        """define width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise TypeError("width must be")

    
