#!/usr/bin/python3
""" define function that returns the JSON representation of a string."""
import json


def to_json_string(my_obj):
    """ return the JSON representation of a string(object)"""
    return json.dumps(my_obj)
