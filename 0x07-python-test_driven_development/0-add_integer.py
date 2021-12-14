#!/usr/bin/python3
"""
Defines an intergers addtion function
"""


def add_integer(a, b=98):
    """
    Returns the addition of a and b as integers.

    a and b must be casted into integers if they are floats.
    """

message = "a must be an integer"
message1 = "b must be an integer"

    if not isinstance(a,(int, float)):
        raise TypeError("message")
    elif not isinstance(b, (int, float)):
        raise TypeError("message1")
    else:
        return (int(a) + int(b))    
