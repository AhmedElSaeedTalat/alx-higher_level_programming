#!/usr/bin/python3
"""TestBase test the Base Class"""
import unittest
from models.square import Square
from models.base import Base
from unittest.mock import patch
from io import StringIO


class TestBase(unittest.TestCase):
    """class TestBase to test BaseClass"""
    def setUp(self):
        """ reset nb ojects before each method """
        Base._Base__nb_objects = 0
        self.s1 = Square(2, 2)
        self.s2 = Square(3, 1, 3)

    def test_display_str(self):
        """test case display and __str__ function"""
        with patch("sys.stdout", new=StringIO()) as output:
            print(self.s2)
            expected_output = '[Square] (2) 1/3 - 3\n'
            self.assertEqual(output.getvalue(), expected_output)

        with patch("sys.stdout", new=StringIO()) as output:
            self.s2.display()
            expected_output = '\n\n\n ###\n ###\n ###\n'
            self.assertEqual(output.getvalue(), expected_output)

        self.assertEqual(self.s1.__str__(), '[Square] (1) 2/0 - 2')
        self.assertEqual(self.s1.area(), 4)
        self.assertEqual(self.s2.area(), 9)

    def test_size(self):
        """test case size"""
        self.s1.size = 5
        self.assertEqual(self.s1.size, 5)

        with self.assertRaises(TypeError):
            self.s1.size = '2'

        with self.assertRaises(ValueError):
            self.s1.size = -5
