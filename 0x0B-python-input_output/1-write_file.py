#!/usr/bin/python3
"""Definition of function that allows file writing"""


def write_file(filename="", text=""):
    """
    Function Returns total characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
