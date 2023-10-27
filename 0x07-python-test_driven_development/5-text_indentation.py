#!/usr/bin/python3
''' This is a documentation of the module including code for test
    it makes text indentation
'''


def text_indentation(text):
    '''
    prints text with special separators : or . or ?
    Args:
        text: string raw text
    Raises:
        TypeError: if text is not a string
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for separator in "?:.":
        text = (separator + "\n\n").join(
            [sentence.strip(" ") for sentence in text.split(separator)])

    print(text, end="")
