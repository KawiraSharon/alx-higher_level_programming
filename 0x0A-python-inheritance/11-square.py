#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Mthds/Attrbts of new square"""

    def __init__(self, size):
        """args size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
