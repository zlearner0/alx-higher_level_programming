#!/usr/bin/python3
'''this module contains function for json object'''

import json


def to_json_string(my_obj):
    '''change python data structure to json string'''
    return json.dumps(my_obj)
