#!/usr/bin/python3
"""Definition of function that reads a text-file"""


def read_file(filename=""):
    """Printing to standard output contents oftext file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
