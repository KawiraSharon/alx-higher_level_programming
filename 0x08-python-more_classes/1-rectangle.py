#!/usr/bin/python3
"""A class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """Definition of the rectangle Constructor
        Args:
        width: width of class rectangle defined; in int
        height: height of new rectangle defined; in int
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be a positive value")
        self._width = value

    @property
    def height(self):
        """Height of rectangle"""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height is not an integer")
        elif (value < 0):
            raise ValueError("height must be a positive value")
        self._height = value
