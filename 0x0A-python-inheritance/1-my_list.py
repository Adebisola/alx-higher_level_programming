#!/usr/bin/python3

""" defines a class that inherits from list """


class MyList(list):
    """ the class that inherits from list """
    def print_sorted(self):
        """ instance method that prints the list in ascending sort """
        print(sorted(self))
