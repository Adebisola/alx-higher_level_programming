#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """defines a Square object"""

        """Args:
        size(an int): the size of the new square object
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
