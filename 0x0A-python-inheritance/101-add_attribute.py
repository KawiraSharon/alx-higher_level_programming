#!/usr/bin/python3
"""Definition of fnctn that takes objects and allows addtion of attributes to them"""


def add_attribute(obj, att, value):
    """New objects take new attributes if possible
    Args:
        obj (any): object being raised for ehich attribute is to be added
        att (str): attribute beign added to the object
        value (any): attribute value
    Raises:
        TypeError: raises error if type cannot be determined
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
