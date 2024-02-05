#!/usr/bin/python3

"""Definition of a class BaseGeometry"""


class BaseGeometry:
    """Description of class"""

    def area(self):
        """Method of class"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method with args"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
