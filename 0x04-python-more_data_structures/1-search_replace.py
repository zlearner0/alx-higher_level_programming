#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''returns a list with replaced elements'''
    if (my_list is None):
        return None
    if (my_list == []):
        return []
    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list
