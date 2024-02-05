#!/usr/bin/python3
"""Func returns True if; object=exactly instance of class, otherwise False"""

def is_same_class(obj, a_class):
    """Returns True/False with resp to condition"""
    if type(obj) == a_class:
        return True

    return False
