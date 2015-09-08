#!/usr/bin/env python
'''
Automated tests using the unittest module.
'''
import unittest

# import the function to test
from exercise import split_string


# definition of testcases
class SplitStringTests(unittest.TestCase):
    def test_dumb(self):
        # Tests for the number of parameters
        with self.assertRaises(TypeError):
            split_string()
        with self.assertRaises(TypeError):
            split_string('')

    def test_empty(self):
        self.assertEqual(split_string('', ''), [])
        self.assertEqual(split_string('', 'abc'), [])
        self.assertEqual(split_string('abc', ''), ['abc'])

    def test_normal(self):
        self.assertEqual(split_string('abacadabra', 'b'), ['a', 'acada', 'ra'])
        self.assertEqual(split_string('aabbaa', 'b'), ['aa', 'aa'])
        self.assertEqual(split_string('abacadabra', 'ab'), ['c', 'd', 'r'])

if __name__ == '__main__':
    print 'This script will test the split_string function from exercise.py .'

    # run the tests
    unittest.main()
