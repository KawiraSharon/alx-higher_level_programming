#!/usr/bin/python3
"""Define function sq."""


def print_square(size):
    """Print a square incl character#

    Args:
        size (int): square height/width
    Raises:
        TypeError: for not int size.
        ValueError: for size<0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
