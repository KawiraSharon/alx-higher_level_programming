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
