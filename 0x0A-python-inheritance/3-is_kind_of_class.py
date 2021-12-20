#!/usr/bin/python3
"""
This module contains method is_kind_of_class
returns True if object is an instance of class that it inherited from
"""


def is_kind_of_class(obj, a_class):
    """
     Args:
        obj: An object.
        a_class: A class
    Return:
        True if obj is an instance of class that it inherited from
    """
    return isinstance(obj, a_class)
