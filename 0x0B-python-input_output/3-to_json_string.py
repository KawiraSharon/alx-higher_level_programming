#!/usr/bin/python3
"""Definition of function that converts string to JSON"""
import json


def to_json_string(my_obj):
    """JSON of str obj is returned"""
    return json.dumps(my_obj)
