#!/usr/bin/python3
"""TestRectangle test the Rectangle Class"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """class TestRectangle to test RectangleClass"""
    def test_print_attributes(self):
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
