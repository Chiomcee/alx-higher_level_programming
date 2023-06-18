#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_nb_objects(self):
        b1 = Base()
        self.assertEqual(Base._Base__nb_objects, 1)

        b2 = Base()
        self.assertEqual(Base._Base__nb_objects, 2)

        b3 = Base()
        self.assertEqual(Base._Base__nb_objects, 3)

if __name__ == '__main__':
    unittest.main()
