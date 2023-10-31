class LockedClass:
    """prevents the user from dynamically creating instance attributes."""
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        '''setting the value of the instance attribute'''
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError
            ("'LockedClass' object has no attribute '{}'".format(name))
