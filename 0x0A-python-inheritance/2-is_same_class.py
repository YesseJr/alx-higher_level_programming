#!/usr/bin/python3
"""
Module containing method is_same_class
returns True if object is exactly an instance of specified class
"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: An object.
        a_class: A class.
    Return:
        True if obj is exactly an instance of specified class
    """
    return type(obj) == a_class
