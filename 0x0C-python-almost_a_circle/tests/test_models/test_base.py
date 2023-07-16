#!/usr/bin/python3
"""TestBase test the Base Class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """class TestBase to test BaseClass"""
    def setUp(self):
        """ reset nb ojects before each method """
        Base._Base__nb_objects = 0

    def test_no_id(self):
        """test case no id is passed"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, 3)

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
        """ """
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
