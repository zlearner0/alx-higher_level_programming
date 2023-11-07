#!/usr/bin/python3
'''this module contains function for json object'''

import json


def load_from_json_file(filename):
    '''give data structure from json file'''
    with open(filename, 'r') as rf:
        return json.load(rf)
