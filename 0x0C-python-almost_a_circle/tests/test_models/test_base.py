#!/usr/bin/python3
"""TestBase test the Base Class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """class TestBase to test BaseClass"""
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
