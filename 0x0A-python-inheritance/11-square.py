#!/usr/bin/python3
"""Rectangle's subclass; sq. defined here"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """New square
        Args:
            size: new sq. size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
