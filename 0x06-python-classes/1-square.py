#!/usr/bin/python3
"""This module defines a Square class with private attributes size"""


class Square:
    """"This represents a Square"""
    def __init__(self, size):
        """Initializing an instance of Square
        Args:
            size: The size of the Square instance
        """
        self.__size = size
