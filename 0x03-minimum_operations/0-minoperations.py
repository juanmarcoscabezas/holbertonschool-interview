#!/usr/bin/python3
"""
Script for minOperations problem
"""


def minOperations(n):
    """
    Finds the min operations
    """
    if n <= 1:
        return 0
    my_str = 'H'
    copy = ''
    iterations = 0
    while len(my_str) < n:
        if n % len(my_str) == 0:
            copy = my_str[:]
            iterations += 1
        my_str = my_str + copy
        iterations += 1
    return iterations
