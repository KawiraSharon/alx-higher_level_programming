#!/usr/bin/python3

"""Definition of class BaseGeometry"""


class BaseGeometry:
    """methods and attributes of class"""

    def area(self):
        """methods of class"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method, functions defined inside class"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
