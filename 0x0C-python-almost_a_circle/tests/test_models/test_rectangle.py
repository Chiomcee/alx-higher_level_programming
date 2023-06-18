#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)
        self.assertEqual(r.id, 50)

    def test_getters_and_setters(self):
        r = Rectangle(10, 20, 30, 40, 50)
        r.width = 100
        r.height = 200
        r.x = 300
        r.y = 400
        r.id = 500
        self.assertEqual(r.width, 100)
        self.assertEqual(r.height, 200)
        self.assertEqual(r.x, 300)
        self.assertEqual(r.y, 400)
        self.assertEqual(r.id, 500)

if __name__ == '__main__':
    unittest.main()
