#!/usr/bin/python3
"""define a character counting function of a written UTF8 text file"""


def write_file(filename="", text=""):
    """Return the number of lines in a text file"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
