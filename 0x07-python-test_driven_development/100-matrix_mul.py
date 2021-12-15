#!/usr/bin/python3
"""
Defines a matrix multiplication function.
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.
      Args:
          m_a (list of lists of ints/floats): The first matrix.
          m_b (list of lists of ints/floats): The second matrix.
    """
message = "m_a can't be empty"
message1 = "m_b can't be empty"
message2 = "m_a must be a list of lists"
message3 = "m_b must be a list of lists"
message4 = "m_a should contain only integers or floats"
message5 = "m_b should contain only integers or floats"
message6 = "each row of m_a must should be of the same size"
message7 = "each row of m_b must should be of the same size"
message8 = "m_a and m_b can't be multiplied"

    if m_a == [] or m_a == [[]]:
        raise ValueError("message")
    if m_b == [] or m_b == [[]]:
        raise ValueError("message1")

    if not isinstance(m_a, list):
        raise TypeError("message")
    if not isinstance(m_b, list):
        raise TypeError("message1")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("message2")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("message3")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("message4")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("essage5")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("message6")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("message7")

    if len(m_a[0]) != len(m_b):
        raise ValueError("message8")

    inverted_b = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        inverted_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
