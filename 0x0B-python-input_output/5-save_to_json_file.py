#!/usr/bin/python3
"""Function that writes a json file"""
import json


def save_to_json_file(my_obj, filename):
    """Writing obj to json file reprsnttn"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
