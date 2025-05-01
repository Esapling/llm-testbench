"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    '''
    return sum(num**2 for num in lst if num > 0 and num % 2 == 1 and isinstance(num, int))

class TestDoubleTheDifference(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)
    
    def test_negative_numbers(self):
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)
    
    def test_single_odd(self):
        self.assertEqual(double_the_difference([9, -2]), 81)
    
    def test_single_zero(self):
        self.assertEqual(double_the_difference([0]), 0)
    
    def test_non_integers(self):
        self.assertEqual(double_the_difference([1.5, 2.5]), 0)

if __name__ == "__main__":
    unittest.main()