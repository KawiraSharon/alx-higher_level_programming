#!/usr/bin/python3
"""Function returns True if obj isinstance; otherwise False"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: object
        a_class: class
    Return:
        True/False
    """
    if issubclass(type(obj), a_class) and (type(obj) is not a_class):
        return True
    return False
