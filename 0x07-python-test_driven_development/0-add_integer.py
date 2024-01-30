#!/usr/bin/python3
"""Definition of integer function addition"""


def add_integer(a, b=98):
    """Return is the addition of a, b

    Typecasting float arguments to ints ahead of addition arithmetic

    Raises:
        TypeError: check whether a/b is typeerror
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
