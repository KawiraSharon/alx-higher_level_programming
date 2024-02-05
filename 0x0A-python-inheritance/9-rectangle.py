#!/usr/bin/python3
"""Class Rectangle inheriting from 7-base-geometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Reactangle class defined here"""

    def __init__(self, width, height):
        """args: self, width, height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area attribute defined"""
        return (self.__width* self.__height)

    def __str__(self):
        """Function performs operator overloading"""
        return "[Rectangle] " + str(self.__width) + '/' + str(self.__height)
