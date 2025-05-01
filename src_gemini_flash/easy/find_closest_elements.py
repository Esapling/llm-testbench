"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest
import math
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        # The problem statement guarantees length at least two,
        # but adding a check makes the function more robust.
        # Based on the prompt, this case shouldn't be reached.
        raise ValueError("Input list must contain at least two numbers")

    min_diff = float('inf')
    closest_pair = None

    # Iterate through all unique pairs of numbers
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            num1 = numbers[i]
            num2 = numbers[j]
            diff = abs(num1 - num2)

            if diff < min_diff:
                min_diff = diff
                closest_pair = (num1, num2)

    # Return the pair in ascending order
    return tuple(sorted(closest_pair))

class TestFindClosestElements(unittest.TestCase):

    def test_example_1(self):
        """Test the first example case."""
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))

    def test_example_2_duplicates(self):
        """Test the second example case with duplicate closest elements."""
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))

    def test_integer_list(self):
        """Test with a list of integers."""
        self.assertEqual(find_closest_elements([5, 2, 8, 1, 9]), (1, 2))

    def test_mixed_signs_and_zero(self):
        """Test with a mix of positive, negative, and zero values."""
        self.assertEqual(find_closest_elements([-1.5, 2.5, 0.0, -0.1]), (-0.1, 0.0))

    def test_two_elements(self):
        """Test with a list containing exactly two elements."""
        self.assertEqual(find_closest_elements([10.0, 20.0]), (10.0, 20.0))
        self.assertEqual(find_closest_elements([5.5, 5.1]), (5.1, 5.5))


# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)