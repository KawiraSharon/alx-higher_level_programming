#!/usr/bin/python3

"""Class of type square defined"""


class Square:
    """Square definition"""

    def __init__(self, size=0):
        """Square initizlized.
        Args:
            size: square size denoted here
        """
        self.size = size

    @property
    def size(self):
        """Getter/setter of current instance/size of the class;square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
