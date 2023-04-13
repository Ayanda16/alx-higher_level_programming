#!/usr/bin/python3

"""Define a subclass square inherited from rectangle"""

Rectangle = __import__('9-rectangle'). Rectangle



class Square(Rectangle):
    """ class square inherited from class rectangle"""

    def __init__(self, size):
        """ initialise class square"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    
    def area(self):
        """define area of class square"""
        return (self.__size ** 2)
