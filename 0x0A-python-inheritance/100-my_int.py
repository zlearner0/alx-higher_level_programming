#!/usr/bin/python3
'''this is documentation for module contains class myINt class
'''


class MyInt(int):
    '''the class invert some operators'''

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
