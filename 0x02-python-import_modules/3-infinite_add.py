#!/usr/bin/env python3

if __name__ == "__main__":
    from sys import argv
    list_len = len(argv)
    if list_len == 1:
        print(0)
    else:
        my_args = argv[1:]
        total_sum = 0
        for item in my_args:
            total_sum += int(item)
print(total_sum)
