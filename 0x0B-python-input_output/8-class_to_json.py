#!/usr/bin/python3
"""Definition of function pyclass to json"""


def class_to_json(obj):
    """Return dictionary represntation for smpledatastrctr"""
    return obj.__dict__
