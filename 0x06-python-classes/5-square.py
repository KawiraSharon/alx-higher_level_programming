#!/usr/bin/python3

"""Definition of class type square"""


class Square:
    """Square representation"""

    def __init__(self, size):
        """Initialization of class type square
        Args:
            size: size of square
        """
        self.size = size

    @property
    def size(self):
        """Getter of current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return is current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Square printed with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
