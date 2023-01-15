#!/usr/bin/python3
"""Define a class Base"""


class Base:
    """"Represents a class with a private attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
