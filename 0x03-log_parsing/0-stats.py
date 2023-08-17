#!/usr/bin/python3
"""
  Python script to read stdin
"""


import sys


def log_parsing():
    """
       Function that reads stdin line by line and
       computes metrics.
    """
    cache = {'200': 0, '301': 0, '400': 0, '401': 0,
             '403': 0, '404': 0, '405': 0, '500': 0}
    total_size = 0
    count = 0

    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) < 5:
            return False
        if len(line_list) == 5:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in cache.keys():
                total_size += size
                count += count

        if count == 10:
            counter = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(cache.items()):
                if value == 0:
                    return False
                else:
                    print('{}: {}'.format(key, value))
