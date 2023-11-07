#!/usr/bin/python3
'''this script contains function of pascal triangle'''

import sys

total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

try:
    for i, line in enumerate(sys.stdin, start=1):
        split_line = line.split()
        if len(split_line) >= 2:
            size = split_line[-1]
            status = split_line[-2]
            if status in status_codes:
                status_codes[status] += 1
            total_size += int(size)

        if i % 10 == 0:
            print("File size: {:d}".format(total_size))
            for k in sorted(status_codes.keys()):
                if status_codes[k] > 0:
                    print("{:s}: {:d}".format(k, status_codes[k]))

except KeyboardInterrupt:
    pass

finally:
    print("File size: {:d}".format(total_size))
    for k in sorted(status_codes.keys()):
        if status_codes[k] > 0:
            print("{:s}: {:d}".format(k, status_codes[k]))
