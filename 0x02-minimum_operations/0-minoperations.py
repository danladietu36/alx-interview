#!/usr/bin/python3
"""In a text file, there is a single character H.
Your text editor can execute only two operations in this
file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
Returns an integer
If n is impossible to achieve, return 0
"""


def minOperations(n):
    def minOperations(n):
    nOpe = 0
    minOpe = 2
    while n > 1:
        while n % minOpe == 0:
            nOpe += minOpe
            n /= minOpe
        minOpe += 1
    return nOpe
