#!/usr/bin/python3
"""define a class"""


class Square:
    """represents a square"""

    def __init__(self, size=0):
        """define a new square object"""
        """
        Args:
        size(int): the size of the square
        """
        self.__size = size

    @property
    def size(self):
        """get to retrieve the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set to set the current size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ return the current area of the square"""
        return (self.__size * self.__size)
