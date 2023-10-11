def best_score(a_dictionary):
    '''give max value of a dictionary'''
    if (max(a_dictionary.values()) is None):
        return None
    if (a_dictionary == {}):
        return 0
    return max(a_dictionary.values())
