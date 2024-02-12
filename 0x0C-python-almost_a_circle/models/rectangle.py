#!/usr/bin/python3
"""Definition rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Definition of class rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Returns nothing
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Getter and setter of width
    @property
    def width(self):
        """Getter for width size
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    # Getter and setter of height
    @property
    def height(self):
        """Getter for height size
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height size
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    # Getter and setter for x variable
    @property
    def x(self):
        """Getter variable x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter variable x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    # Getter and setter for y variable
    @property
    def y(self):
        """Getter variable y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter y variable
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Method to returns obj rectangle area
        """
        return self.width * self.height

    def display(self):
        """prints to stdout
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + self.width * '#')

    def __str__(self):
        """overrides str method
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        """Method order of args for rectangle object
        """
        dict_order = ['id', 'width', 'height', 'x', 'y']
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
        """Method that returns a dictionary with
        """
        dict_order = ['x', 'y', 'id', 'height', 'width']
        dict_attrs = {}
        for key in dict_order:
            dict_attrs[key] = getattr(self, key)
        return dict_attrs
