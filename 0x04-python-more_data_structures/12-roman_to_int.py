#!/usr/bin/python3
def roman_to_int(roman_string):
    '''change from roman number to integer'''
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    decimal = 0
    for i in range(len(roman_string)):
        current_value = roman_map[roman_string[i]]
        if i < len(roman_string) - 1 and roman_map[roman_string[
                i + 1]] > current_value:
            decimal -= current_value
        else:
            decimal += current_value
    return decimal
