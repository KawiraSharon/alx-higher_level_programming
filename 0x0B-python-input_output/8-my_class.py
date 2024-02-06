#!/usr/bin/python3
"""Class Myclass definition"""


class MyClass:
    """Class and method definition"""

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)
