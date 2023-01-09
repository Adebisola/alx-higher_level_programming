#!/usr/bin/python3
""" define a function that if an object is an instance of a
    specified class or its instance
"""


def is_kind_of_class(obj, a_class):
    """ function that checks if object is an instance of a class or
    the class the specified class inherited from
    """
    return isinstance(obj, a_class)
