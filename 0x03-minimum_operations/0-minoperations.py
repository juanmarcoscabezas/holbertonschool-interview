#!/usr/bin/python3
"""
Script for minOperations problem
"""


def minOperations(n):
    """
    Finds the min operations
    """
    if n <= 0:
        return 0
    my_str = 'H'
    copy = ''
    iterations = 0
    while len(my_str) < n:
        copy = copy_str(my_str)
        my_str = paste_str(my_str, copy)
        iterations += 2
        print(my_str)
    return iterations


def paste_str(my_str, copy):
    """
    Makes the paste
    """
    return my_str + copy


def copy_str(my_str):
    """
    Makes the copy
    """
    return my_str
