#!/usr/bin/python3
import importlib


def magic_calculation(a, b):
    if a < b:
        add = importlib.import_module("magic_calculation_102").add
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
        return c
    else:
        return importlib.import_module("magic_calculation_102").sub(a, b)
