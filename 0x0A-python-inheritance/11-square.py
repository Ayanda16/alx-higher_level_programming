#!/usr/bin/python3
"""define subclass square based on rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square that inherits from rectangle"""
    def __init__(self, size):

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """print square description"""
        string = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return string
