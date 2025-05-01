"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest
from typing import List

def double_the_difference(lst: List[float]) -> int:
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.

    double_the_difference([1, 3, 2, 0]) == 1^2 + 3^2 = 1 + 9 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 9^2 = 81
    double_the_difference([0]) == 0

    If the input list is empty, return 0.
    """
    if not lst:
        return 0

    sum_of_squares = 0
    for num in lst:
        # Check if the number is an integer, positive, and odd
        if isinstance(num, int) and num > 0 and num % 2 != 0:
            sum_of_squares += num ** 2

    return sum_of_squares

class TestDoubleTheDifference(unittest.TestCase):

    def test_example_1(self):
        """Test the first example case with positive odd numbers."""
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)

    def test_example_2_negative_numbers(self):
        """Test the second example case with negative numbers."""
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)

    def test_empty_list(self):
        """Test with an empty input list."""
        self.assertEqual(double_the_difference([]), 0)

    def test_mixed_types_and_signs(self):
        """Test with a mix of integers, non-integers, positive and negative numbers."""
        # Positive odd integers: 1, 5. Sum of squares: 1^2 + 5^2 = 1 + 25 = 26
        self.assertEqual(double_the_difference([1, 2, 3.5, 4, 5, -7, 0]), 26)

    def test_only_even_and_negative(self):
        """Test with a list containing only even numbers and negative numbers."""
        self.assertEqual(double_the_difference([2, 4, -6, -8, 0]), 0)

# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)