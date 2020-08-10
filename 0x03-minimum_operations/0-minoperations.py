#!/usr/bin/python3


def minOperations(n):
    my_str = 'H'
    copy = ''
    iterations = 0
    while len(my_str) < n:
        copy = copy_str(my_str, copy)
        my_str = paste_str(my_str, copy)
        iterations += 1
        print(my_str)
    return iterations


def paste_str(my_str, copy):
    return my_str + copy


def copy_str(my_str, copy):
    copy = my_str
    return copy
