#!/usr/bin/python3
"""
Defines a function that prints a square with the character #.
"""


def print_square(size):
    """
    Prints the square with the character #

    Args:
        size (int): The height/width of the square
    """

    message = "size must be an integer"
    message1 = "size must be >= 0"

    if not isinstance(size, int):
        raise TypeError("message")

    if size < 0:
        raise ValueError("message1")

        print(("#" * size + "\n") * size, end="")
