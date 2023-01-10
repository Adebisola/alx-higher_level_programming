#!/usr/bin/python3
"""defines a Class to JSON function i.e
    a function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
"""


def class_to_json(obj):
    """obj is an instance of a Class"""
    return obj.__dict__
