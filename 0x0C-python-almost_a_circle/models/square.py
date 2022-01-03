#!/usr/bin/python3
"""
Defines a square class.
Inherits from Rectangle;
"""


from models.rectangle import Rectangle
"""
Represent a square.
"""


class Square(Rectangle):
    """
    defines class Square; inherits from class Rectangle
    Inherited Attributes:
        id
        __weight        __height
        __x             __y
    Class Attributes:
        size
    Inherted Methods:
        Base.init(self, id=None)
        Rectangle.init(self, width, height, x=0, y=0, id=None)
        update(self, *args, **kwargs)
        width(self)      width(self, value)
        height(self)     height(self, value)
        x(self)          x(self, value)
        y(self)          y(self, value)
        area(self)       display(self)
    Methods:
        __str__
        __init__(self, size, x=0, y=0, id=None)
        update(self, *args, **kwargs)
        size(self)       size(self, value)
        to_dictionary(self)
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square.
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        Getter size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter size - sets width and height as size
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Prints [Square] (<id>) <x>/<y> - <size>
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.size)

    def update(self, *args, **kwargs):
        """
        If args: set attributes in this order: id, width, height, x, y
        If no args given: set attributes according to kwargs
        """
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.size = v
                elif k == 2:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Return dictionary representation
        """
        dict = {}
        dict["id"] = self.id
        dict["size"] = self.size
        dict["x"] = self.x
        dict["y"] = self.y
        return dict
