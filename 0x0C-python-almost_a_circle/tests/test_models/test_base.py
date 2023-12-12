#!/usr/bin/python3
'''this module tests Base class'''

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import unittest


class test_Base(unittest.TestCase):
    '''tesing Base class via unittest'''

    def setUp(self):
        '''when action needed before every test'''
        pass

    def tearDown(self):
        '''when action needed after every test'''
        Base._Base__nb_objects = 0

    # task1

    def test_id(self):
        '''test id of base instances'''
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    # task 15

    def test_to_json_string_rec(self):
        '''test to transform from rectangle object to json string'''
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        jsn_d = Base.to_json_string([dictionary])

        self.assertEqual(
            dictionary, {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8})
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(
            jsn_d, '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')
        self.assertEqual(type(jsn_d), str)

    # task 15

    def test_to_json_string_sq(self):
        '''test to transform from square object to json string'''
        r1 = Square(10, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])

        self.assertEqual(dictionary, {'id': 1, 'size': 10, 'x': 2, 'y': 8})
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(
            json_dictionary, '[{"id": 1, "size": 10, "x": 2, "y": 8}]')
        self.assertEqual(type(json_dictionary), str)

        # task 16

    def test_save_to_file(self):
        ''' test save object to file'''
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        r1r2 = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        with open("Rectangle.json", "r") as file:
            filecont = file.read()

        self.assertEqual(filecont, r1r2)

    # task 17

    def test_from_json_string(self):
        '''test transforming from string to object'''
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

        self.assertEqual(type(list_input), list)
        self.assertEqual(type(json_list_input), str)
        self.assertEqual(type(list_output), list)
        self.assertEqual(list_output, list_input)

    # task 18
    def test_create(self):
        '''test creating an object for dictionary'''
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    # task 19
    def test_load_from_file(self):
        '''test loading string list to python list object'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list1 = [r1, r2]
        Rectangle.save_to_file(list1)
        list2 = Rectangle.load_from_file()
        if len(list1) == len(list2):
            isequal = True
        for dict1, dict2 in zip(list1, list2):
            if dict1 == dict2:
                isequal = True
        self.assertTrue(isequal)

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list3 = [s1, s2]
        Square.save_to_file(list3)
        list4 = Square.load_from_file()
        if len(list3) == len(list4):
            isequal = True
        for dict3, dict4 in zip(list3, list4):
            if dict3 == dict4:
                isequal = True
        self.assertTrue(isequal)

    def test_csv_save_load(self):
        '''test load and save in csv format'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list1 = [r1, r2]
        Rectangle.save_to_file_csv(list1)
        list2 = Rectangle.load_from_file_csv()
        if len(list1) == len(list2):
            isequal = True
        for dict1, dict2 in zip(list1, list2):
            if dict1 == dict2:
                isequal = True
        self.assertTrue(isequal)

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list3 = [s1, s2]
        Square.save_to_file_csv(list3)
        list4 = Square.load_from_file_csv()
        if len(list3) == len(list4):
            isequal = True
        for dict3, dict4 in zip(list3, list4):
            if dict3 == dict4:
                isequal = True
        self.assertTrue(isequal)
