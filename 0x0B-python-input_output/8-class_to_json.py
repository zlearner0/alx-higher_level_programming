#!/usr/bin/python3
'''this script contains function for json object'''


def class_to_json(obj):
    """ dictionary description of an object"""
    d = {}
    for k, v in obj.__dict__.items():
        if isinstance(v, (int, bool, str, list, dict)):
            d[k] = v
    return d
