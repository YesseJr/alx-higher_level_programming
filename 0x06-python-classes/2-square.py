#!/usr/bin/python3
"""This module defines a class Square by Private instance attribute: size"""


class Square:
    """"This represents a class Square"""
    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
