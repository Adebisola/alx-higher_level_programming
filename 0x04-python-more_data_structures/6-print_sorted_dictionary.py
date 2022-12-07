#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """print a dictionary by ordered keys."""
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
        """[print("{}: {}".format(key, a_dictionary[k]))
        for key in sorted(a_dictionary)]"""
