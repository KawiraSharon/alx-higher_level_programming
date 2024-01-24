#!/usr/bin/python3
''' A Module that creates a Square object '''


class Square:
    """ Object template creation"""

    def __init__(self, size=0):
        '''
            Init method; to initialize instance of class

        @self:
            Instance of class

        @size:
            Size of the square, unsigned data type in c
        '''
        if type(size) is int:
            if size < 0:
                raise ValueError('Size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('Size must be an integer')
