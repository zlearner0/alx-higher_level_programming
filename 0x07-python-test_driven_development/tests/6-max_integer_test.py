#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    ''' testing function max_integer function for the critical inputs'''

    def test_normal_integer(self):
        self.assertEqual(max_integer([5, 9, -1]), 9)
        self.assertEqual(max_integer([-5, -9, -1]), -1)
        self.assertEqual(max_integer([5.26, 9.3, -1.258]), 9.3)

    def test_empty(self):
        """test for intering a data types"""
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(()), None)
        self.assertEqual(max_integer({}), None)

    def test_float_inf(self):
        """test float(inf)"""
        self.assertEqual(max_integer([float('inf'), 8574227]),
                         float('inf'))

    def test_string(self):
        """test for intering a string"""
        result = max_integer("string")
        self.assertEqual(result, "t")

    def test_single_float(self):
        """test for intering a float"""
        with self.assertRaises(TypeError):
            max_integer(987.56)

    def test_single_int(self):
        """test for intering an integer"""
        with self.assertRaises(TypeError):
            max_integer(98)

    def test_dict(self):
        """test for intering a dictionary"""
        with self.assertRaises(TypeError):
            max_integer([{"name": "ted", "age": 25}, {1: "a"}])

    def test_hybrid_list(self):
        """hybrid list"""
        with self.assertRaises(TypeError):
            max_integer([[], [20], [2], [30, 40], [500, 400, 300], "string"])
