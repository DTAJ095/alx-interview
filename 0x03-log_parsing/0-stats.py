#!/usr/bin/python3
""" Log parsing
Script that reads stdin line by line and computes metrics
"""
import sys


if __name__ == "__main__":
    total_size = 0
    counter = 0
    status_code = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }

    def print_stats():
        print("File size: {}".format(total_size))
        for key, value in sorted(status_code.items()):
            if value != 0:
                print("{}: {}".format(key, value))

    try:
        for line in sys.stdin:
            data = line.split()
            if len(data) > 2:
                total_size += int(data[-1])
                if data[-2] in status_code:
                    status_code[data[-2]] += 1
                counter += 1
                if counter == 10:
                    print_stats()
                    counter = 0
        print_stats()
    except KeyboardInterrupt:
        print_stats()
        raise
