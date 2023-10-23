#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    j = 0
    i = 0
    while (j != x):

        try:
            print("{:d}".format(my_list[j]), end="")
            i += 1
        except (ValueError, TypeError):
            pass
        except IndexError:
            break
        j += 1

    print()
    return i
