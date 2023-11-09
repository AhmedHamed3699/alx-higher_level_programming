#!/usr/bin/python3
"""A module for Reading stdin line by line and computes stats."""
import sys

status = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}
size = 0
line_no = 0


def print_stat():
    """Print status."""
    print(f'File size: {size}')
    for stat, value in sorted(status.items()):
        if value != 0:
            print(f'{stat}: {value}')


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            line_list = line.split()
            if len(line_list) > 1:
                if line_list[-2] in status:
                    status[line_list[-2]] += 1
                size += int(line_list[-1])
            line_no += 1
            if line_no == 10:
                print_stat()
                line_no = 0
        print_stat()

    except KeyboardInterrupt:
        print_stat()
