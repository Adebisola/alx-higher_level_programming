#!/usr/bin/python3
""" defines a class MyInt that inherits from int and inverts the
    operators == and !=
"""


class MyInt(int):
    """ inverts the operators == and !="""

    def __eq__(self, value):
        """overides == operator with != behaviour."""
        return self.real != value

    def __ne__(self, value):
        """overides =! operator with == behaviour"""
        return self.real == value
