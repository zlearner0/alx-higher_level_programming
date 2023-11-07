#!/usr/bin/python3
'''this module contains function for json object'''

import json


def from_json_string(my_str):
    '''transform from json to python data structure'''
    return json.loads(my_str)
