#!/usr/bin/python3
"""
Defines a function that ptint a name
"""


from typing import Type


def say_my_name(first_name, last_name=""):
    """
    Prints out a name.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.
    """

    message = "first_name must be a string"
    message1 = "last_name must be a string"

    if not isinstance(first_name, str):
        raise TypeError("message")

    if not isinstance(last_name, str):
        raise TypeError("message1")

    print("My name is {:s} {:s}".format(first_name, last_name)    
