#!/usr/bin/python3
'''this module contains function for json object'''

import json


def save_to_json_file(my_obj, filename):
    '''change data structure to string and send to file'''
    with open(filename, 'w') as wf:
        json.dump(my_obj, wf)
