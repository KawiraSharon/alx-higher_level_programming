#!/usr/bin/python3

"""Definition of class MyList"""


class MyList(list):
    """Class's mthds definition"""

    def print_sorted(self):
        """List printed in ascending order"""
        print(sorted(self))
