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

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

        print(("#" * size + "\n") * size, end="")
