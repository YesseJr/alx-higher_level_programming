#!/usr/bin/python3
"""
Reads from standard input and computes metrics

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
     Total file size up to that point.
     Count of read status codes up to that point.
"""


import sys


def print_size_and_codes(size, stat_codes):
    """Print accumulated metrics.
    
    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {:d}".format(size))
    for k, v in sorted(stat_codes.items()):
        if v:
            print("{:s}: {:d}".format(k, v))


def parse_stdin_and_compute():
    size = 0
    lines = 0
    stat_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                  "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for line in sys.stdin:
            fields = list(map(str, line.strip().split(" ")))
            size += int(fields[-1])
            if fields[-2] in stat_codes:
                stat_codes[fields[-2]] += 1
            lines += 1
            if lines % 10 == 0:
                print_size_and_codes(size, stat_codes)
    except KeyboardInterrupt:
        print_size_and_codes(size, stat_codes)
        raise

    print_size_and_codes(size, stat_codes)


parse_stdin_and_compute()
