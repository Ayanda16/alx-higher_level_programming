#!/usr/bin/python3
''' class rectangle that defines a rectangle'''


class Rectangle():

    def __init___(self, width, height):
        ''' initialising a new rectangle'''
        self.width = width
        self.height = height

    def width(self):
        '''retrieve the width'''
        return self._width

    def width(self, value):
        ''' set the width properties '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value
