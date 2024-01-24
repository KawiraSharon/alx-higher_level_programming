#!/usr/bin/python3

"""Definition of class named square"""


class Square:
    """Square is denoted here"""

    def __init__(self, size=0):
        """Square is Initialized.
        Args:
            size: square size int
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Square size returned"""
        return (self.__size * self.__size)
