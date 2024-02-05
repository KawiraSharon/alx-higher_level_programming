#!/usr/bin/python3
"""Define inherited class"""


class Mylist(list):
    """Sorts builtin list"""

    def print_sorted(self):
        """list output in order that ascends"""
        print(sorted(self))
