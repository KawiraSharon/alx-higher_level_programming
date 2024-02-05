#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Mthds/Attrbts of new square"""
    self.integer_validator("size", size)
    super().__init__(size, size)
    self.__size = size
