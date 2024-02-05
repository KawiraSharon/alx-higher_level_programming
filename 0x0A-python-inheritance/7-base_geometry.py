#!/usr/bin/python3
"""Class Basegeometry"""


class BaseGeometry:
    """Class BaseGeometry taking methods"""

    def area(self):
        """Raise exception not named"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Methods are functions defined inside class
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
