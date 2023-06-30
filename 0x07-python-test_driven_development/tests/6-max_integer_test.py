#!/usr/bin/python3
""" unit test """

import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMax(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([]), None)
