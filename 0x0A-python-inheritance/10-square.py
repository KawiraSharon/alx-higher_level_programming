#!/usr/bin/python3
"""Classs square that inherits frm above class rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Individual class methods/attributes"""

    def __init__(self, size):
        """Args are size"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
