#!/usr/bin/python3
"""
This module defines a Pascal's Triangle function.
"""


def pascal_triangle(n):
    """
    Represent Pascal's Triangle of size n.
Return:
        empty list [] if n <= 0
    if n is 8, we should expect:
            [1]
            [1, 1]
            [1, 2, 1]
            [1, 3, 3, 1]
            [1, 4, 6, 4, 1]
            [1, 5, 10, 10, 5, 1]
            [1, 6, 15, 20, 15, 6, 1]
            [1, 7, 21, 35, 35, 21, 7, 1]
    """
    if n <= 0:
        return []
        if n == 1:
            return [[1]]

    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
