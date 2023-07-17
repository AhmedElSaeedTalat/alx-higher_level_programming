#!/usr/bin/python3
"""TestBase test the Base Class"""
import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO
import inspect


class TestSquare(unittest.TestCase):
    """class TestSquare to test SquareClass"""
    def setUp(self):
        """ reset nb ojects before each method """
        Base._Base__nb_objects = 0
        self.s1 = Square(2, 2)
        self.s2 = Square(3, 1, 3)

    def test_docs(self):
        """ test if it has docs """
        self.assertIsNotNone(Square.__doc__, "Square has no docs")
        for method in inspect.getmembers(Square):
            self.assertIsNotNone(method.__doc__, "Method has no docs")

    def test_subcls(self):
        """ check if cls is a subclass"""
        Base._Base__nb_objects = 0
        s = Square(10)
        self.assertTrue(isinstance(s, (Square, Rectangle, Base)))
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(issubclass(Square, Rectangle))

    def test_invalid_size(self):
        """ test invalid size"""
        with self.assertRaises(TypeError):
            s = Square('2')

        """ passing negative number """
        with self.assertRaises(ValueError):
            s = Square(-4)

    def test_noArgs(self):
        """ test no args """
        with self.assertRaises(TypeError):
            s = Square()

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

    def test_update(self):
        """test update function"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.__str__(), '[Square] (10) 0/0 - 5')

        s1.update(1, 2)
        self.assertEqual(s1.__str__(), '[Square] (1) 0/0 - 2')

        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), '[Square] (1) 3/0 - 2')

        s1.update(1, 2, 3, 4, size=5)
        self.assertEqual(s1.__str__(), '[Square] (1) 3/4 - 2')

        s1.update(x=12)
        self.assertEqual(s1.__str__(), '[Square] (1) 12/4 - 2')

        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), '[Square] (1) 12/1 - 7')

        s1.update(size=7, id=89, y=1)
        with patch("sys.stdout", new=StringIO()) as output:
            print(s1)
            expected_output = '[Square] (89) 12/1 - 7\n'
            self.assertEqual(output.getvalue(), expected_output)

    def test_to_dictionary(self):
        """ test to_dictionary function"""
        Base._Base__nb_objects = 0
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 1, 'x': 2, 'size': 10, 'y': 1})
        self.assertEqual(type(s1_dictionary), dict)
