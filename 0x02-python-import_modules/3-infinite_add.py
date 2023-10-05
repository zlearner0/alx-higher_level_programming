# !/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    args = argv[1:]
    sum = 0
    for item in args:
        sum += int(item)
print(sum)
