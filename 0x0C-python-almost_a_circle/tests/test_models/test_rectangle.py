#!/usr/bin/python3
"""TestRectangle test the Rectangle Class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch
import io


class TestRectangle(unittest.TestCase):
    """class TestRectangle to test RectangleClass"""
    def setUp(self):
        """ reset nb ojects before each method """
        Base._Base__nb_objects = 0

    def test_docs(self):
        """ test if it has docs """
        self.assertEqual(len(Rectangle.__doc__) > 1, True)

    def test_attributes(self):
        """test case print attributes passed"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

        r2 = Rectangle(10, 2)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

        r4 = Rectangle(10, 5, 3, 6, 12)
        self.assertEqual(r4.width, 10)
        self.assertEqual(r4.height, 5)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 6)

    def test_setters(self):
        """test case for setters"""
        r1 = Rectangle(10, 5, 3, 6, 12)
        r1.height = 2
        r1.width = 4
        r1.x = 3
        r1.y = 8
        r1.id = 303

        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 8)
        self.assertEqual(r1.id, 303)

    def test_raises(self):
        """test error when setting attributes"""
        with self.assertRaises(TypeError):
            Rectangle(5, '2')

        with self.assertRaises(TypeError):
            r1 = Rectangle(5, 5)
            r1.width = '2'

        with self.assertRaises(TypeError):
            Rectangle('2', 5)

        with self.assertRaises(TypeError):
            r1 = Rectangle(5, 5)
            r1.height = '2'

        with self.assertRaises(ValueError):
            Rectangle(5, -10)

        with self.assertRaises(ValueError):
            r1 = Rectangle(5, 4)
            r1.width = 0

        with self.assertRaises(ValueError):
            Rectangle(-5, 10)

        with self.assertRaises(ValueError):
            r1 = Rectangle(5, 4)
            r1.height = 0

        with self.assertRaises(ValueError):
            Rectangle(5, 10, -5, 0)

        with self.assertRaises(ValueError):
            r1 = Rectangle(5, 4, 0, 0)
            r1.x = -5

        with self.assertRaises(ValueError):
            Rectangle(5, 10, 0, -7)

        with self.assertRaises(ValueError):
            r1 = Rectangle(5, 4, 0, 7)
            r1.y = -7

    def test_area(self):
        """ test area"""
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_display(self):
        """test display function"""
        r1 = Rectangle(4, 4)
        with patch('sys.stdout', new=io.StringIO()) as output:
            r1.display()
            self.assertEqual(output.getvalue(), '####\n####\n####\n####\n')

        r1 = Rectangle(2, 3, 2, 2)
        with patch('sys.stdout', new=io.StringIO()) as output:
            r1.display()
            expected_output = '\n\n  ##\n  ##\n  ##\n'
            self.assertEqual(output.getvalue(), expected_output)

        r2 = Rectangle(3, 2, 1, 0)
        with patch('sys.stdout', new=io.StringIO()) as output:
            r2.display()
            expected_output = ' ###\n ###\n'
            self.assertEqual(output.getvalue(), expected_output)

    def test_str(self):
        """test __str__ function"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        with patch('sys.stdout', new=io.StringIO()) as output:
            print(r1)
            self.assertEqual(output.getvalue(), "[Rectangle] (12) 2/1 - 4/6\n")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r2.__str__(), '[Rectangle] (1) 1/0 - 5/5')

    def test_update(self):
        """ test update function """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 10/10 - 10/10')

        r1.update(89, 2)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 10/10 - 2/10')

        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 10/10 - 2/3')

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 4/10 - 2/3')

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 4/5 - 2/3')

    def test_update1(self):
        """ test update function with kwargs"""
        r2 = Rectangle(10, 10, 10, 10)
        r2.update(height=1)
        self.assertEqual(r2.__str__(), '[Rectangle] (1) 10/10 - 10/1')

        r2.update(width=1, x=2)
        self.assertEqual(r2.__str__(), '[Rectangle] (1) 2/10 - 1/1')

        r2.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r2.__str__(), '[Rectangle] (89) 3/1 - 2/1')

        r2.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r2.__str__(), '[Rectangle] (89) 1/3 - 4/2')

    def test_to_dictionary(self):
        """test to_dictionary function"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        expected_output = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1_dictionary, expected_output)
        self.assertEqual(type(r1_dictionary), dict)

        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        with patch('sys.stdout', new=io.StringIO()) as output:
            print(r2)
            self.assertEqual(output.getvalue(), "[Rectangle] (1) 1/9 - 10/2\n")
