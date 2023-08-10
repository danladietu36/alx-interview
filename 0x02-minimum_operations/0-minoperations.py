#!/usr/bin/python3


"""
    The letter H is the only character in a text file.
    There are only two operations that your text editor can do on 
	this file: Copy All and Paste. Write a method that calculates 
	given a number n.
    the least amount of processes necessary to produce exactly 
	n H characters in the file.
"""


def minOperations(n):
    nOpe = 0
    minOpe = 2
    while n > 1:
        while n % minOpe == 0:
            nOpe += minOpe
            n /= minOpe
        minOpe += 1
    return nOpei
