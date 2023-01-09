#!/usr/bin/python3


""" defines a function which checks instances of a class """
def is_same_class(obj, a_class):
    """ function which checks if an object is the exact instances of a class """
    if type(obj) is a_class:
        return True
    return False
