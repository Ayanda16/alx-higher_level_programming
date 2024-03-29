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

    def update(self, *args, **kwargs):
        """update square"""
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        """return a representation of square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def to_dictionary(self):
        """return the dictionary representation of a square"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
