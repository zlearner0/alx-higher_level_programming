#!/usr/bin/python3
'''this script contains function of object attributes'''


class Student:
    '''contains attributes and method for them'''

    def __init__(self, first_name, last_name, age):
        '''initialize attributes of the object'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''dictionary for object attributes'''
        result = {}
        for i, j in self.__dict__.items():
            if isinstance(j, (int, bool, str, list, dict)):
                result[i] = j
        return result
