#!/usr/bin/python3
"""Definition of name-printing function."""


def say_my_name(first_name, last_name=""):
    """name'll be printed

    Args:
        first_name (str): 1st name being printed
        last_name (str): 2nd last name being printed
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
