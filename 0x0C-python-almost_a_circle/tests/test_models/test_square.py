#!/usr/bin/python3

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """ """
    def test_square_area(self):
        """ """
        sq1 = Square(5)
        self.assertEqual(sq1.area(), 25)
        sq2 = Square(8)
        self.assertEqual(sq2.area(), 64)

    def test_square_update(self):
        """ """
        sq1 = Square(5)
        sq1.update(6, 10)
        self.assertEqual(sq1.id, 6)
        self.assertEqual(sq1.area(), 100)
        sq1.update(7, 2, 3)
        self.assertEqual(sq1.area(), 4)

    def test_square_str(self):
        """ """
        sq1 = Square(5)
        self.assertEqual(str(sq1), "[Square] (5) 0/0 - 5")

    def test_square_size_property(self):
        """ """
        sq1 = Square(5)
        self.assertEqual(sq1.size, 5)
        sq1.size = 7
        self.assertEqual(sq1.width, 7)
        self.assertEqual(sq1.height, 7)

    def test_square_size_property(self):
        """ """
        sq1 = Square(5)
        self.assertEqual(sq1.size, 5)
        sq1.size = 7
        self.assertEqual(sq1.width, 7)
        self.assertEqual(sq1.height, 7)

    def test_square_size_property_error(self):
        """ """
        sq1 = Square(5)
        with self.assertRaises(TypeError):
            sq1.size = "9"
