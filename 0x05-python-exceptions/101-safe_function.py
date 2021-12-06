#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
    except:
        stderr.write("Exception: {}\n".format(e))
        return None
