#!/usr/bin/python3
"""
Defines an intergers addtion function
"""


def add_integer(a, b=98):
    """
    Returns the addition of a and b as integers
    """

    if not isinstance(a,(int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))    
