#!usr/bin/python3
def search_replace(my_list, search, replace):
    '''returns a list with replaced elements'''
    if (not my_list):
        return None
    for item in my_list:
        if item == search:
            my_list[my_list.index(item)] = replace
    return my_list
