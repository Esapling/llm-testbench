"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import math
import unittest

def sum_squares(lst):
    return sum(math.ceil(x)**2 for x in lst)

class TestSumSquares(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sum_squares([1,2,3]), 14)
        self.assertEqual(sum_squares([1,4,9]), 98)
        self.assertEqual(sum_squares([1,3,5,7]), 84)

    def test_floats(self):
        self.assertEqual(sum_squares([1.4,4.2,0]), 29)

if __name__ == "__main__":
    unittest.main()
