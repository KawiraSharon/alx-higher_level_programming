#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Mthds/Attrbts of new square"""

    def __init__(self, size):
        """
        Args:
           size: int
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
