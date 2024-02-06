#!/usr/bin/python3
"""Definition of Json file"""
import json


def load_from_json_file(filename):
    """json file allows creation of python object"""
    with open(filename) as f:
        return json.load(f)
