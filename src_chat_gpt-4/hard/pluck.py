def pluck(arr):
    candidates = [(val, idx) for idx, val in enumerate(arr) if val % 2 == 0]
    if not candidates:
        return []
    smallest = min(candidates)
    return [smallest[0], smallest[1]]

import unittest

class TestPluck(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(pluck([4,2,3]), [2,1])
    def test_case2(self):
        self.assertEqual(pluck([1,2,3]), [2,1])
    def test_empty(self):
        self.assertEqual(pluck([]), [])