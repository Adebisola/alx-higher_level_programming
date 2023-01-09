#!/usr/bin/python3
""" defines a class with a public instance method """


class BaseGeometry:
    """ a class BaseGeometry """
    def area(self):
        """ an unimplemented instance method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
