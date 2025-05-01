"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest
import math
from typing import List

def sum_squares(lst: List[float]) -> int:
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6


    """
    if not lst:
        return 0

    total_sum_of_squares = 0
    for num in lst:
        rounded_up = math.ceil(num)
        total_sum_of_squares += rounded_up ** 2

    return total_sum_of_squares

class TestSumSquares(unittest.TestCase):

    def test_example_1_integers(self):
        """Test the first example case with integers."""
        self.assertEqual(sum_squares([1, 2, 3]), 14)

    def test_example_4_floats_and_zero(self):
        """Test the fourth example case with floating points and zero."""
        self.assertEqual(sum_squares([1.4, 4.2, 0]), 29)

    def test_example_5_negatives_and_integers(self):
        """Test the fifth example case with negatives and integers."""
        self.assertEqual(sum_squares([-2.4, 1, 1]), 6)

    def test_empty_list(self):
        """Test with an empty input list."""
        self.assertEqual(sum_squares([]), 0)

    def test_mixed_floats_near_integers(self):
        """Test with mixed positive and negative floating-point numbers near integers."""
        # ceil(-1.1) = -1, (-1)^2 = 1
        # ceil(-2.9) = -2, (-2)^2 = 4
        # ceil(3.0) = 3, 3^2 = 9
        # Sum = 1 + 4 + 9 = 14
        self.assertEqual(sum_squares([-1.1, -2.9, 3.0]), 14)
        # ceil(0.1) = 1, 1^2 = 1
        # ceil(0.9) = 1, 1^2 = 1
        # ceil(-0.1) = 0, 0^2 = 0
        # ceil(-0.9) = 0, 0^2 = 0
        # Sum = 1 + 1 + 0 + 0 = 2
        self.assertEqual(sum_squares([0.1, 0.9, -0.1, -0.9]), 2)


# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)