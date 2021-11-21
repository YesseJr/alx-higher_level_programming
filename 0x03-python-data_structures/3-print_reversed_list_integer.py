#!/usr/bin/python3
# What does the Isinstance function do?
# The isinstance() function returns True if the specified object is of the specified type, otherwise False
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        for i in reversed(my_list):
            print("{:d}".format(i))
