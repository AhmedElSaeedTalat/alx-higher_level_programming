#!/usr/bin/python3
""" Unittest for max_integer([..]) """


import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMax(unittest.TestCase):
    def test_max_integer_ordered(self):
        """
            def test_max_integer_ordered(self): test function to
            test max_integer function for an ordered list
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer_empty(self):
        """
            def test_max_integer_empty(self): test function to test max_integer
            function for an empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_max_integer_singleValue(self):
        """
            def test_max_integer_singleValue(self): test function to
            test max_integer function for a single value
        """
        self.assertEqual(max_integer([5]), 5)

    def test_max_integer_repeatedValue(self):
        """
            def test_max_integer_repeatedValye(self): test function to test
            max_integer function a repeated value in a list
        """
        self.assertEqual(max_integer([1, 2, 9, 9, 8, 1]), 9)

    def test_max_integer_negative(self):
        """
            def test_max_integer_negative(self): test function to test
            max_integer function with a list with negative values
        """
        self.assertEqual(max_integer([-8, -2, -9]), -2)

    def test_max_integer_floats(self):
        """
            def test_max_integer_negative(self): test function to test
            max_integer function with a list of float values
        """
        self.assertEqual(max_integer([8.2, 2.32, 9.233]), 9.233)

    def test_max_integer_string(self):
        """
            def test_max_integer_negative(self): test function to test
            max_integer function with a string that represents a list
        """
        self.assertEqual(max_integer("name"), 'n')

    def test_max_integer_listStrings(self):
        """
            def test_max_integer_negative(self): test function to test
            max_integer function with a list of strings
        """
        self.assertEqual(max_integer(["first", "second", "third"]), "third")
