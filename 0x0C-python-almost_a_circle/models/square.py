#!/usr/bin/python3
"""class square that inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """define class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialise square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get square size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """return a representation of square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
