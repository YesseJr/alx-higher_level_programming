#!/usr/bin/python3
"""
This module contains BaseGeometry
with public instance method area and integer_validation
"""


class BaseGeometry:
    """
    Reprsent base geometry.

    """
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates input
        Args:
            name (str): assumed always a string
            value (int): greater than 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
