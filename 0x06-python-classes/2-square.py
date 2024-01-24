#!/usr/bin/python3
"""Square class type created"""


class Square:
    """Square defined here"""

    def __init__(self, size=0):
        """
        Initialization of square

            Args:
                size: square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
