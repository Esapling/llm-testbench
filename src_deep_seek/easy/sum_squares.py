"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import math
import unittest

def sum_squares(lst):
    """Return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    """
    return sum(math.ceil(num)**2 for num in lst)

class TestSumSquares(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(sum_squares([1, 2, 3]), 14)
    
    def test_example2(self):
        self.assertEqual(sum_squares([1, 4, 9]), 98)
    
    def test_odd_numbers(self):
        self.assertEqual(sum_squares([1, 3, 5, 7]), 84)
    
    def test_decimal_numbers(self):
        self.assertEqual(sum_squares([1.4, 4.2, 0]), 29)
    
    def test_negative_numbers(self):
        self.assertEqual(sum_squares([-2.4, 1, 1]), 6)

if __name__ == "__main__":
    unittest.main()