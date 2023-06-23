#!/usr/bin/python3

import unittest
from models.square import Square
"""
    Test cases for the module square
"""


class TestSquare(unittest.TestCase):
    """Testing square"""
    def test_square_area(self):
        """Testing area attribute """
        sq1 = Square(5)
        self.assertEqual(sq1.area(), 25)
        sq2 = Square(8)
        self.assertEqual(sq2.area(), 64)

    def test_square_update(self):
        """attribute update """
        sq1 = Square(5)
        sq1.update(6, 10)
        self.assertEqual(sq1.id, 6)
        self.assertEqual(sq1.area(), 100)
        sq1.update(7, 2, 3)
        self.assertEqual(sq1.area(), 4)

    def test_square_str(self):
        """Square str testing"""
        sq1 = Square(5)
        self.assertEqual(str(sq1), "[Square] (5) 0/0 - 5")

    def test_square_size_property(self):
        """Testing side"""
        sq1 = Square(5)
        self.assertEqual(sq1.size, 5)
        sq1.size = 7
        self.assertEqual(sq1.width, 7)
        self.assertEqual(sq1.height, 7)

    def test_square_size_property(self):
        """Testing side"""
        sq1 = Square(5)
        self.assertEqual(sq1.size, 5)
        sq1.size = 7
        self.assertEqual(sq1.width, 7)
        self.assertEqual(sq1.height, 7)

    def test_square_size_property_error(self):
        """type error testing"""
        sq1 = Square(5)
        with self.assertRaises(TypeError):
            sq1.size = "9"