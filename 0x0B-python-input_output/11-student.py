#!/usr/bin/python3
"""Definition of Class Student"""


class Student:
    """Student reprsnttn"""

    def __init__(self, first_name, last_name, age):
        """New student being initialized"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Args:
            attrs: attributes being represented
        """
        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Args:
            json: key pairs replacing attributes(dictionary)
        """
        for k, v in json.items():
            setattr(self, k, v)
