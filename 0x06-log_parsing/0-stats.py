#!/usr/bin/python3

"""
cript that reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
"""


import sys


total_file_size = 0
codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
num_lines = 0


def print_data():
    print('File size: {}'.format(total_file_size))
    for key in codes.keys():
        if codes[key] > 0:
            print('{}: {}'.format(key, codes[key]))
    return 0

if __name__ == '__main__':
    try:
        for line in sys.stdin:
            line = line.split(' ')
            size = line[-1]
            total_file_size += int(size)

            codes[line[-2]] += 1
            if num_lines == 9:
                num_lines = print_data()
            else:
                num_lines += 1
    except (KeyboardInterrupt, EOFError):
        print_data()
