#!/usr/bin/python3
"""
Defines text indentation function
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each ".", "?", and ":"
    """
    message = "text must be a string"
    
    if not isinstance(text, str):
        raise TypeError("message")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    revised = "\n".join(list_lines)
    print(revised, end="")
