#!/usr/bin/python3
"""Definition of class MyInt that inherits from the standard int."""


class MyInt(int):
    """Inversion of operators of int; !=."""

    def __eq__(self, value):
        """Opeartor that's != behavior is overridden."""
        return self.real != value

    def __ne__(self, value):
        """Operators != that've got == behavior overriden."""
        return self.real == value
