#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if isinstance(a_dictionary, dict):
        match = list(key for key in a_dictionary.keys() if a_dictionary[key] is value)
        for key in match:
                del a_dictionary[key]
        return a_dictionary
