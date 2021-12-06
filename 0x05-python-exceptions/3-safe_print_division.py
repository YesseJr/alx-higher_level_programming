#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        waython = a / b
    except ZeroDivisionError:
        waython = None
    finally:
        print("Inside result: {}".format(waython))
    return waython
