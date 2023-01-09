#!/usr/bin/python3
"""Defines a function that checks if an object is an instance a class"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of the specified class.
    """
    if type(obj) is a_class:
        return True
    return False
