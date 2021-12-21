#!/usr/bin/python3
"""
This module defines a file-writing function.
"""


def write_file(filename="", text=""):
    """
    writes to text file and returns num chars written
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
