#!/usr/bin/python3
""" unit test class """


import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMax(unittest.TestCase):
    def test_max_integer(self):
        """
            def test_max_integer(self): test function to test max_integer
            function
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([]), None)
