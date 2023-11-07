#!/usr/bin/python3
'''this script contains function of pascal triangle'''


def append_after(filename="", search_string="", new_string=""):
    with open(filename, "r+") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.truncate()
