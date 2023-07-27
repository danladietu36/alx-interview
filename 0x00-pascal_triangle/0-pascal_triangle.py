#!/usr/bin/python3
""" A python script to compute Pascal's triangle for n number
"""


def pascal_triangle(n):
    """
    A pascal triangle that returns a list of integers representing
    the Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
