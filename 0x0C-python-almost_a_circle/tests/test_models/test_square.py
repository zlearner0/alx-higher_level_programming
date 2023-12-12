#!/usr/bin/python3
'''this module tests Square class'''

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import unittest


class test_Square(unittest.TestCase):
    '''tesing Square class via unittest'''

    def setUp(self):
        '''when action needed before every test'''
        pass

    def tearDown(self):
        '''when action needed after every test'''
        Base._Base__nb_objects = 0

    # task2

    def test_rc_id(self):
        '''test id of rectangle instances'''
        r1 = Square(10)
        r2 = Square(2)
        r3 = Square(10, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    # task3
    def test_err_msg(self):
        '''test errors raised for setters'''
        r1 = Square(10)
        with self.assertRaises(TypeError):
            r1.size = 'string'
            r1.width = 'string'
            r1.height = 'string'
            r1.x = 'string'
            r1.y = 'string'
            Square("0")
            Square(1, "-1", 2, 14)
            Square(1, 2, "2", 15)

        with self.assertRaises(ValueError):
            r1 = Square(10, 2)
            r1.size = -2
            r1.size = 0
            r1.width = -1
            r1.width = 0
            r1.height = -2
            r1.height = 0
            r1.x = -3
            r1.y = -4
            Square(0, 1)
            Square(-1, 1)
            Square(0, 0)
            Square(1, 0)
            Square(1, -1)
            Square(1, 2, -1, -2, 14)
            Square(1, 2, 1, -2, 15)

    # task4

    def test_area(self):
        '''test area of square'''
        r1 = Square(10)
        r3 = Square(5, 0, 0, 12)
        self.assertEqual(r1.area(), 100)
        self.assertEqual(r3.area(), 25)

    # task5 & 7

    def test_display(self):
        ''' test visual shape'''
        from io import StringIO
        import sys
        r4 = Square(3, 4, 4)
        expected_output = ' \n \n \n \n    ###\n    ###\n    ###\n'
        with StringIO() as buffer:
            sys.stdout = buffer  # redirect stdout to the buffer
            r4.display()  # call the method that prints the display output
            actual_output = buffer.getvalue()  # get the output from the buffer
        self.assertEqual(actual_output, expected_output)
        sys.stdout = sys.__stdout__  # restore stdout

    # task6
    def test_str(self):
        '''test string representation of the object'''
        r4 = Square(4, 2, 1, 12)
        r5 = Square(5, 1)
        self.assertEqual(str(r4), '[Square] (12) 2/1 - 4')
        self.assertEqual(str(r5), '[Square] (1) 1/0 - 5')

    # task8

    def test_args_update(self):
        ''''test *args when updating object attributes'''
        r1 = Square(10, 10, 10)
        self.assertEqual(str(r1), '[Square] (1) 10/10 - 10')
        r1.update(89)
        self.assertEqual(str(r1), '[Square] (89) 10/10 - 10')
        r1.update(89, 2)
        self.assertEqual(str(r1), '[Square] (89) 10/10 - 2')
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), '[Square] (89) 3/10 - 2')
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), '[Square] (89) 3/4 - 2')
        r1.update(89, 2, 4, 5)
        self.assertEqual(str(r1), '[Square] (89) 4/5 - 2')

    # task9

    def test_kwargs_update(self):
        ''''test *kwarg when updating object attributes'''
        r1 = Square(10, 10, 10)
        self.assertEqual(str(r1), '[Square] (1) 10/10 - 10')
        r1.update(size=1)
        self.assertEqual(str(r1), '[Square] (1) 10/10 - 1')
        r1.update(size=1, x=2)
        self.assertEqual(str(r1), '[Square] (1) 2/10 - 1')
        r1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(str(r1), '[Square] (89) 3/1 - 2')
        r1.update(x=1, size=4, y=3)
        self.assertEqual(str(r1), '[Square] (89) 1/3 - 4')

    # task14

    def test_to_dictionary(self):
        ''' test when updating with to_dictonary() method'''
        s1 = Square(10, 2, 1)
        self.assertEqual(str(s1), '[Square] (1) 2/1 - 10')
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 1, 'size': 10, 'x': 2, 'y': 1})
        self.assertEqual(type(s1_dictionary), dict)

        s2 = Square(1, 1)
        self.assertEqual(str(s2), '[Square] (2) 1/0 - 1')
        s2.update(**s1_dictionary)  # unpack dictionary
        self.assertEqual(str(s2), '[Square] (1) 2/1 - 10')
        self.assertFalse(s1 == s2, False)
