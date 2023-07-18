#!/usr/bin/python3
"""TestBase test the Base Class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from unittest.mock import patch
from io import StringIO
import inspect


class TestBase(unittest.TestCase):
    """class TestBase to test BaseClass"""
    def setUp(self):
        """ reset nb ojects before each method """
        Base._Base__nb_objects = 0

    def test_docs(self):
        """ test if it has docs """
        self.assertIsNotNone(Base.__doc__, "has no docs")
        self.assertIsNotNone('models.base'.__doc__, "Module has no docs")
        for method in inspect.getmembers(Base):
            self.assertIsNotNone(method.__doc__, "has no docs")

    def test_no_id(self):
        """test case no id is passed"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, 3)

        with self.assertRaises(TypeError):
            b4 = Base(12, 12)

    def test_passed_id(self):
        """test case passed id"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_to_json_string(self):
        """ test to_json_string function"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        expected = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(json_dictionary, expected)
        self.assertEqual(type(json_dictionary), str)

        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, '[]')
        self.assertEqual(type(json_dictionary), str)

        """ case argument is None """

        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, '[]')
        self.assertEqual(type(json_dictionary), str)

    def test_save_to_file(self):
        """ save to file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            expected = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},\
 {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
            self.assertEqual(file.read(), expected)

        """ case argument is None """

        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            expected = '[]'
            self.assertEqual(file.read(), expected)

        Rectangle.save_to_file([])

        with open("Rectangle.json", "r") as file:
            expected = '[]'
            self.assertEqual(file.read(), expected)

        Square.save_to_file(None)

        with open("Square.json", "r") as file:
            expected = '[]'
            self.assertEqual(file.read(), expected)

    def test_from_json_string(self):
        """ test from_json_string function """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)
        expected = [
            {'height': 4, 'width': 10, 'id': 89},
            {'height': 7, 'width': 1, 'id': 7}
        ]
        self.assertEqual(list_output, expected)

        """ case argument is None """
        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])

    def test_create(self):
        """ test create functions """

        """ case to create instance & update attributes """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)
        self.assertEqual(type(r2), Rectangle)
        with patch('sys.stdout', new=StringIO()) as output:
            print(r2)
            self.assertEqual(output.getvalue(), '[Rectangle] (1) 1/0 - 3/5\n')
        self.assertEqual(r2.__str__(), '[Rectangle] (1) 1/0 - 3/5')

    def test_load_from_file(self):
        """ test load_from_file function """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()
        expected = '[Rectangle] (1) 2/8 - 10/7'
        self.assertEqual(list_rectangles_output[0].__str__(), expected)
        expected = '[Rectangle] (2) 0/0 - 2/4'
        self.assertEqual(list_rectangles_output[1].__str__(), expected)

    def test_load_no_file(self):
        """ no file passed"""
        list_output = Rectangle.load_from_file()
        self.assertEqual(list_output, [])

    def test_csv_functions(self):
        """ test csv functions"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        l_output = Rectangle.load_from_file_csv()
        self.assertEqual(l_output[0].__str__(), '[Rectangle] (1) 2/8 - 10/7')
        self.assertEqual(l_output[1].__str__(), '[Rectangle] (2) 0/0 - 2/4')

        """ case of list of Squares """

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        list_output = Square.load_from_file_csv()
        self.assertEqual(list_output[0].__str__(), '[Square] (5) 0/0 - 5')
        self.assertEqual(list_output[1].__str__(), '[Square] (6) 9/1 - 7')
