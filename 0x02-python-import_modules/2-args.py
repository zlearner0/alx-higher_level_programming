# !/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        args = argv[1:]
        print("{:d} argument:".format(len(args)))
        for item, val in enumerate(args, start=1):
            print("{:d}: {}".format(item, val))
    else:
        args = argv[1:]
        print("{:d} arguments:".format(len(args)))
        for item, val in enumerate(args, start=1):
            print("{:d}: {}".format(item, val))
