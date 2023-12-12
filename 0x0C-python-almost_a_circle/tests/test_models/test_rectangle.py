#!/usr/bin/python3
'''this module tests Rectangle class'''

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import unittest


class test_Rectangle(unittest.TestCase):
    '''tesing Rectangle class via unittest'''

    def setUp(self):
        '''when action needed before every test'''
        pass

    def tearDown(self):
        '''when action needed after every test'''
        Base._Base__nb_objects = 0

    # task2

    def test_rc_id(self):
        '''test id of rectangle instances'''
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    # task3
    def test_err_msg(self):
        '''test errors raised for setters'''
        r1 = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r1.width = 'string'
            r1.height = 'string'
            r1.x = 'string'
            r1.y = 'string'
            Rectangle("0", 1)
            Rectangle(1, "1")
            Rectangle("0", "0")
            Rectangle(1, 2, "-1", 2, 14)
            Rectangle(1, 2, 1, "2", 15)

        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2)
            r1.width = -1
            r1.width = 0
            r1.height = -2
            r1.height = 0
            r1.x = -3
            r1.y = -4
            Rectangle(0, 1)
            Rectangle(-1, 1)
            Rectangle(0, 0)
            Rectangle(1, 0)
            Rectangle(1, -1)
            Rectangle(1, 2, -1, -2, 14)
            Rectangle(1, 2, 1, -2, 15)

    # task4

    def test_area(self):
        '''test area of rectangle'''
        r1 = Rectangle(10, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.area(), 20)
        self.assertEqual(r3.area(), 20)

    # task5 & 7

    def test_display(self):
        ''' test visual shape'''
        from io import StringIO
        import sys
        r4 = Rectangle(3, 2, 4, 4)
        expected_output = ' \n \n \n \n    ###\n    ###\n'
        with StringIO() as buffer:
            sys.stdout = buffer  # redirect stdout to the buffer
            r4.display()  # call the method that prints the display output
            actual_output = buffer.getvalue()  # get the output from the buffer
        self.assertEqual(actual_output, expected_output)
        sys.stdout = sys.__stdout__  # restore stdout

    # task6
    def test_str(self):
        '''test string representation of the object'''
        r4 = Rectangle(4, 6, 2, 1, 12)
        r5 = Rectangle(5, 5, 1)
        self.assertEqual(str(r4), '[Rectangle] (12) 2/1 - 4/6')
        self.assertEqual(str(r5), '[Rectangle] (1) 1/0 - 5/5')

    # task8

    def test_args_update(self):
        ''''test *args when updating object attributes'''
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), '[Rectangle] (1) 10/10 - 10/10')
        r1.update(89)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 10/10')
        r1.update(89, 2)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 2/10')
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 2/3')
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), '[Rectangle] (89) 4/10 - 2/3')
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), '[Rectangle] (89) 4/5 - 2/3')

    # task9

    def test_kwargs_update(self):
        ''''test *kwarg when updating object attributes'''
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), '[Rectangle] (1) 10/10 - 10/10')
        r1.update(height=1)
        self.assertEqual(str(r1), '[Rectangle] (1) 10/10 - 10/1')
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), '[Rectangle] (1) 2/10 - 1/1')
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), '[Rectangle] (89) 3/1 - 2/1')
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), '[Rectangle] (89) 1/3 - 4/2')

    # task13

    def test_to_dictionary(self):
        ''' test when updating with to_dictonary() method'''
        s1 = Rectangle(4, 5, 2, 1)
        self.assertEqual(str(s1), '[Rectangle] (1) 2/1 - 4/5')
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(
            s1_dictionary, {'id': 1, 'width': 4, 'height': 5, 'x': 2, 'y': 1})
        self.assertEqual(type(s1_dictionary), dict)

        s2 = Rectangle(1, 2, 1)
        self.assertEqual(str(s2), '[Rectangle] (2) 1/0 - 1/2')
        s2.update(**s1_dictionary)  # unpack dictionary
        self.assertEqual(str(s2), '[Rectangle] (1) 2/1 - 4/5')
        self.assertFalse(s1 == s2, False)
