#!/usr/bin/python3
# 6-from_json_string.py
"""Definition of a function to convrt JSON->object"""
import json


def from_json_string(my_str):
    """Return Python obj reprsnttn of a JSON string."""
    return json.loads(my_str)
