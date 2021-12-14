#!/usr/bin/python3
"""
Defines the function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of the matrix and returns new matrix

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    """

    message = "matrix must be a matrix (list of lists) of integers/floats"
    message1 = "Each row of the matrix must have the same size"
    message2 = "div must be a number"
    message3 = "division by zero"

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("message")
    
    if not isinstance (div, (int, float)):
        raise TypeError("message2")

    if div == 0:
        raise ZeroDivisionError("message3")

        new_matrix = []
        for row in matrix:
            if type(row) is not list:
                raise TypeError("message")

            if row_len = -1:
              row_len = len(row)
              if row_len = 0:
                  raise TypeError("message")

            else:
                if row_len != len(row):
                    raise TypeError("message1")

        new_row = []
        for ele in row:
            if type(ele) is int or float:
                new_row.append(round(ele / div, 2))
            else:
                raise TypeError("message")

        new_matrix.append(new_row)   
      return new_matrix       
