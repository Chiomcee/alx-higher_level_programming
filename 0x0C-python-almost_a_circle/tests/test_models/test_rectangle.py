#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init(self):
        r1 = Rectangle(10, 20, 30, 40, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 30)
        self.assertEqual(r1.y, 40)
        self.assertEqual(r1.id, 1)

    def test_width(self):
        r1 = Rectangle(10, 20)
        r1.width = 30
        self.assertEqual(r1.width, 30)

        with self.assertRaises(TypeError):
            r1.width = "hello"

        with self.assertRaises(ValueError):
            r1.width = -10

    def test_height(self):
        r1 = Rectangle(10, 20)
        r1.height = 30
        self.assertEqual(r1.height, 30)

        with self.assertRaises(TypeError):
            r1.height = "hello"

        with self.assertRaises(ValueError):
            r1.height = -10

    def test_x(self):
        r1 = Rectangle(10, 20)
        r1.x = 30
        self.assertEqual(r1.x, 30)

        with self.assertRaises(TypeError):
            r1.x = "hello"

        with self.assertRaises(ValueError):
            r1.x = -10

    def test_y(self):
        r1 = Rectangle(10, 20)
        r1.y = 30
        self.assertEqual(r1.y, 30)

        with self.assertRaises(TypeError):
            r1.y = "hello"

        with self.assertRaises(ValueError):
            r1.y = -10


if __name__ == '__main__':
    unittest.main()
