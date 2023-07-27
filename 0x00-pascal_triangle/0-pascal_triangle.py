#!/usr/bin/python3
""" A python script to compute Pascal's triangle for n number
"""


def pascal_triangle(n):
    """
    A pascal triangle that returns a list of integers representing
    the Pascal's triangle of n.
    """

    triangle = []

    if (n <= 0):
        return triangle

    for x in range(n):
        tmp_list = []

        for y in range(x + 1):
            if y == 0 or y == x:
                tmp_list.append(1)
            else:
                tmp_list.append(triangle[x-1][y-1] + triangle[x-1][y])
        triangle.append(tmp_list)
    return (traingle)
