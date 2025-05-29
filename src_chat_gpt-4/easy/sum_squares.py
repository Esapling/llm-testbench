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

    #------------ Phase 2 Tests ------------
    def test_empty_list(self):
        self.assertEqual(sum_squares([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_squares([-1,-2,-3]), 14)
    
    def test_zero_value(self):
        self.assertEqual(sum_squares([0]), 0)
        self.assertEqual(sum_squares([0, 0, 0]), 0)
        self.assertEqual(sum_squares([-1, 0, 1]), 2)
 
    def test_decimal_numbers(self):
        self.assertEqual(sum_squares([1.5, 2.5, 3.5]), 29)

    def test_large_numbers(self):
        self.assertEqual(sum_squares([1000, 2000, 3000]), 14000000)
        self.assertEqual(sum_squares([1e6, 2e6, 3e6]), 14000000000000)

    def test_small_numbers(self):
        self.assertEqual(sum_squares([0.1, 0.2, 0.3]), 3) # 1 + 1 + 1
        self.assertEqual(sum_squares([0.0001, 0.0002]), 2)# 1 + 1

if __name__ == "__main__":
    unittest.main()

