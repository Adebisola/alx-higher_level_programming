#!/usr/bin/python3
""" defines a function that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """returns an object froms represented by a JSON string"""
    return json.loads(my_str)
