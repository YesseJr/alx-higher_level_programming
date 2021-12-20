#!/usr/bin/python3
"""
This module defines a function that adds attributes to objects.
"""


def add_attribute(obj, att, value):
    """
    Add a new attribute to an object if possible.
    Args:
        att (str): The name of the attribute to add to obj.
        obj (any): The object to add an attribute to.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
