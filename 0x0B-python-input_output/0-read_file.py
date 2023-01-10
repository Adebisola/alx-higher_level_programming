#!/usr/bin/python3
"""define a function that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """ a function that prints content of a text file (UTF8) to stdout:"""
    with open(filename, encoding="utf-8") as MyFile:
        print(MyFile.read(), end="")
