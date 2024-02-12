#!/usr/bin/python3
"""Module for dfntn of square object"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Method for sq. intialization
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Method that returns a string"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))

    @property
    def size(self):
        """Getter for sq. size
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter for square
        """
        self.width = value
        self.heigth = value

    def update(self, *args, **kwargs):
        """
        Return:
           nothing

        """
        dict_order = ['id', 'size', 'x', 'y']
        if args is not None and bool(args) is True:
            i = 0
            for key in dict_order:
                try:
                    setattr(self, key, args[i])
                except IndexError:
                    pass
                i += 1
        else:
            for key in dict_order:
                try:
                    setattr(self, key, kwargs[key])
                except KeyError:
                    pass

    def to_dictionary(self):
        """Method to return dictionary
        """
        dict_order = ['id', 'x', 'size', 'y']
        dict_attrs = {}
        for key in dict_order:
            dict_attrs[key] = getattr(self, key)
        return dict_attrs
