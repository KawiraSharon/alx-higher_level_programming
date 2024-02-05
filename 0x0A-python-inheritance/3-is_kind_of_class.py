#!/usr/bin/python3
"""Func return True if objis instance or False if otherwise"""


def is_kind_of_class(obj, a_class):
    """
    Return True or False with respct to condition
    """
    if isinstance(obj, a_class):
        return True
    return False
