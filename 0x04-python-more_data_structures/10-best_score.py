#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    x = list(a_dictionary.keys())[0]
    biggest_score = a_dictionary[x]
    for key, value in a_dictionary.items():
        if value > biggest_score:
            biggest_score = value
            x = key
            return (x)
