#!/usr/bin/python3
"""Definition of a function that appends file to another"""


def append_write(filename="", text=""):
    """
    Total characters appended are returned
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
