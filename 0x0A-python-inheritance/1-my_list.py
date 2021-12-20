#!/usr/bin/python3
"""
This module defines an inherited list class MyList.
"""


class MyList(list):
    """
    Implements sorted printing for the built-in list class.
    """

    def print_sorted(self):
        """
        Print a list of ints sorted ascending order.
        """
        print(sorted(self))
