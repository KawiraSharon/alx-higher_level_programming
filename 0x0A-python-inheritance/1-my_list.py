#!/usr/bin/python3

"""Define inherited class"""


class Mylist(list):
    """Sorts builtin list"""

    def print_sorted(self):
        """List output in order that ascends"""
        print(sorted(self))
