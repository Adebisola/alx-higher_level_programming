#!/usr/bin/python3
"""defines a function that appends a string to the end of a UTF8 text file"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file (UTF8) and
        returns the number of characters added:
    """
    with open(filename, mode="a", encoding="UTF-8") as myFile:
        return myFile.write(text)
