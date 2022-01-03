#!/usr/bin/python3
"""
Defines a Base class.
It contains private class __nb_objects and class constructor __init__
"""

import json
import csv
import turtle

class Base:
    """
    Defines class Base.
    This class will be the "base" of all other classes in this project.

    Class Attributes:
       __nb_objects

    Methods:
       __init__(self, id=None)
    Static Methods:
       from_json_string(json_string)
       to_json_string(list_dictionaries)
    Class Methods:
       save_to_file(cls, list_objs)
       save_to_file_csv(cls, list_objs)
       load_from_file(cls)
       load_from_file_csv(cls)
       create(cls, **dictionary)
       draw(cls, list_rectangles, list_squares):
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize id, increment class attribute if no id and set as id
        Args:
            id (int): The identity of the new Base.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


            @staticmethod
            def from_json_string(json_string):
                """
                Returns Python obj of JSON string representation
                """
                if json_string is None or len(json_string) == 0:
                    json_string = "[]"
                return json.loads(json_string)

            @staticmethod
            def to_json_string(list_dictionaries):
                """
                Returns JSON string representation of list dict
                """
                if list_dictionaries is None:
                    list_dictionaries = []
                return json.dumps(list_dictionaries)

            @classmethod
            def save_to_file(cls, list_objs):
                """
                Save json strings of all instances into file
                """
                objs = []
                if list_objs is not None:
                    for o in list_objs:
                        objs.append(cls.to_dictionary(o))
                filename = cls.__name__ + ".json"
                with open(filename, "w") as f:
                    f.write(cls.to_json_string(objs))

            @classmethod
            def save_to_file_csv(cls, list_objs):
                """
                Write the CSV serialization of a list of objects to a file.
                        Args:
                            list_objs (list): A list of inherited Base instances.
                """
                filename = cls.__name__ + ".csv"
                with open(filename, 'w', newline='') as f:
                    writer = csv.writer(f)
                    for o in list_objs:
                        if cls.__name__ == "Rectangle":
                            writer.writerow([o.id, o.width, o.height, o.x, o.y])
                        if cls.__name__ == "Square":
                            writer.writerow([o.id, o.size, o.x, o.y])

            @classmethod
            def load_from_file(cls):
                """
                Returns list of instances
                """
                filename = cls.__name__ + ".json"
                l = []
                try:
                    with open(filename, "r") as f:
                        instances = cls.from_json_string(f.read())
                    for i, dic in enumerate(instances):
                        l.append(cls.create(**instances[i]))
                except:
                    pass
                return l

            @classmethod
            def load_from_file_csv(cls):
                """
                Return a list of classes instantiated from a CSV file.
                        Reads from `<cls.__name__>.csv`.
                        Returns:
                            If the file does not exist - an empty list.
                            Otherwise - a list of instantiated classes.
                """
                objs = []
                filename = cls.__name__ + ".csv"
                with open(filename, 'r', newline='') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if cls.__name__ == "Rectangle":
                            dic = {"id": int(row[0]),
                                   "width": int(row[1]),
                                   "height": int(row[2]),
                                   "x": int(row[3]),
                                   "y": int(row[4])}
                        if cls.__name__ == "Square":
                            dic = {"id": int(row[0]),
                                   "size": int(row[1]),
                                   "x": int(row[2]),
                                   "y": int(row[3])}
                        o = cls.create(**dic)
                        objs.append(o)
                return objs

            @classmethod
            def create(cls, **dictionary):
                """
                Returns instance with attributes already set
                """
                if cls.__name__ == "Square":
                    alx = cls(1)
                if cls.__name__ == "Rectangle":
                    alx = cls(1, 1)
                alx.update(**dictionary)
                return alx

            @classmethod
            def draw(cls, list_rectangles, list_squares):
                """
               Draw Rectangles and Squares using the turtle module.
               Args:
               list_rectangles (list): A list of Rectangle objects to draw.
               list_squares (list): A list of Square objects to draw.
               """
            cellie = turtle.Screen()
            newyear = turtle.Pen()
            figures = list_rectangles + list_squares

            for fig in figures:
               newyear.up()
               newyear.goto(fig.x, fig.y)
               newyear.down()
               newyear.forward(fig.width)
               newyear.right(90)
               newyear.forward(fig.height)
               newyear.right(90)
               newyear.forward(fig.width)
               newyear.right(90)
               newyear.forward(fig.height)
               newyear.right(90)

               cellie.exitonclick()
        
         