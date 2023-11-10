#!/usr/bin/python3
'''this module contains class Square'''


# from rectangle import Rectangle
# Rectangle = __import__('rectangle').Rectangle
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class represents square shape'''

    def __init__(self, size, x=0, y=0, id=None):
        '''initialize the object attributes'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''size getter'''
        return self.width

    @size.setter
    def size(self, value):
        '''size setter'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''updates the object attrubutes'''
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

        if args is None or args == ():
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''dictionary representation for the object'''
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
