#!/usr/bin/python3
"""Module base"""
import json
import csv
from collections import OrderedDict
import turtle


class Base:
    """Definition of base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Return:
           Nothing.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return JSON string
        """
        if list_dictionaries is None or bool(list_dictionaries) is False:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries)
            return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Return:
            Nothing
        """
        filename = "{}.json".format(cls.__name__)
        list_dictionaries = []
        if list_objs is not None:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                list_dictionaries.append(dictionary)
            json_string = Base.to_json_string(list_dictionaries)
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Return:
           Python object

        """
        if json_string is None or bool(json_string) is False:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return:
           Instance with set attribute
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Method to return list """
        filename = "{}.json".format(cls.__name__)
        instance_list = []
        try:
            with open(filename, 'r') as f:
                json_string = f.read()
                dictionary_list = cls.from_json_string(json_string)
                for item in dictionary_list:
                    instance = cls.create(**item)
                    instance_list.append(instance)
        except FileNotFoundError:
            return instance_list
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Method CSV """
        filename = "{}.csv".format(cls.__name__)
        data = []
        if list_objs is not None:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                data.append(dictionary)
        rectangle_header = ['id', 'width', 'height', 'x', 'y']
        square_header = ['id', 'size', 'x', 'y']
        with open(filename, mode='w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                if cls.__name__ == 'Rectangle':
                    result = csv.DictWriter(f, fieldnames=rectangle_header)
                elif cls.__name__ == 'Square':
                    result = csv.DictWriter(f, fieldnames=square_header)
                result.writeheader()
                result.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """ Csv deserialization """
        filename = "{}.csv".format(cls.__name__)
        instance_list = []
        try:
            with open(filename) as f:
                result = csv.DictReader(f)
                for row in result:
                    row = dict(row)
                    for key in row:
                        row[key] = int(row[key])
                    instance = cls.create(**row)
                    instance_list.append(instance)
        except FileNotFoundError:
            return instance_list
        return instance_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Mtd to draw

        Args:
           list_squares: objects square list
           list_rectangles: objects rec list

        Return:
                Nothing
        """
        s = turtle.getscreen()
        t = turtle.Turtle()

        turtle.title("My first draw with python and tutle module")

        t.shape("turtle")
        turtle.bgcolor("black")

        t.pen(pencolor="blue", fillcolor="white", pensize=5, speed=1)
        for instance in list_rectangles:
            t.pen(pencolor="blue", fillcolor="white", pensize=5, speed=1)
            data = instance.to_dictionary()
            t.home()
            t.setpos(data['x'], data['y'])
            t.pd()
            for i in range(2):
                t.forward(data['width'])
                t.left(90)
                t.forward(data['height'])
                t.left(90)
            t.pu()

        t.pen(pencolor="red", fillcolor="white", pensize=5, speed=0.5)
        for instance in list_squares:
            data = instance.to_dictionary()
            t.home()
            t.setpos(data['x'], data['y'])
            t.pd()
            for i in range(4):
                t.forward(data['size'])
                t.left(90)
            t.pu()
        turtle.getscreen()._root.mainloop()
