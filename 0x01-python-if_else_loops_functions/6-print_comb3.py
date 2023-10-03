#!/usr/bin/python3
j = 0
for i in range(1, 100):
    if i < 10 or i // 10 < i % 10:
        for j in range(i + 1, 100):
            if j < 10 or j // 10 < j % 10:
                print("{:02d}".format(i), end=", ")
                break
        if j == 99:
            print("{:02d}".format(i))
