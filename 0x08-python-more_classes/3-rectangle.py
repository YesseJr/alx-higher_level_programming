#!/usr/bin/python3
"""This module contains class Rectangle with private attribute width and height"""


class Rectangle:
    """
        Rectangle Class
    """

    def __init__(self, width=0, height=0):
        """ Initializing an instance of ``Rectangle``
        Args:
            width (int, optional): The width of the ``Rectangle`` instance.
            height (int, optional): The height of the ``Rectangle`` instance.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """
            Returns a string representation of ``Rectangle`` instance using '#'
        """
        if self.width is 0 or self.height is 0:
            return ""
        else:
            return (('#' * self.width + '\n') * (self.height - 1) +
                    '#' * self.width)

    @property
    def width(self):
        """ int: width of the ``Rectangle`` instance. """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ int: height of the ``Rectangle`` instance. """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area of the ``Rectangle`` instance. """
        return self.height * self.width

    def perimeter(self):
        """ Returns the perimeter of the ``Rectangle`` instance. """
        return (self.height * 2) + (self.width * 2)
