#!/usr/bin/python3
"""Define a class rectangle that inherits from,BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
   """class rectangle that inherits from BaseGeometry"""
   def __init__(self, width,height):
       """initialise rectangle with width and height"""
       self.integer_validator("width", width)
       self.__width = width
       self.integer_validator("height", height)
       self.__height = height
