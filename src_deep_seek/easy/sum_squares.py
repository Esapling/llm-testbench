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
        #------------ Phase 2 Tests ------------
    def test_empty_list(self):
        self.assertEqual(sum_squares([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_squares([-1,-2,-3]), 14)
    
    
    def test_zero_value(self):
        self.assertEqual(sum_squares([0]), 0)
        self.assertEqual(sum_squares([0, 0, 0]), 0)
        self.assertEqual(sum_squares([-1, 0, 1]), 2)
    
    def test_non_numerical_input(self):
        with self.assertRaises(TypeError):
            sum_squares(["a", "b", "c"])
        with self.assertRaises(TypeError):
            sum_squares([None, True, False])
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