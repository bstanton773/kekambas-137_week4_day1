import unittest

from whiteboard import solution

class MatchTestCase(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(solution([1,1,0,1,1,1]),3)
    def test_example_two(self):
        self.assertEqual(solution([1,0,1,1,0,1]),2)
    def test_zero(self):
        self.assertEqual(solution([0,0,0]),0)
    def test_lots_of_ones(self):
        self.assertEqual(solution([1,1,1,1,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]),17)
