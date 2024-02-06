#!/usr/bin/python3
"""Definition of class named Student"""


class Student:
    """Representation of student."""

    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name: Student's first name str
            last_name: Student's name str
            age: student age, in int
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Student's dictionary represnttn"""
        return self.__dict__
