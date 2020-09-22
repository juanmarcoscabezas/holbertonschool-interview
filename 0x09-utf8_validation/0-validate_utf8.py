#!/usr/bin/python3
"""
Validate UTF8
"""


def validUTF8(data):
    for number in data:
        if number > 255:
            return False
    return True
