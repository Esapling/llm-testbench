"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest
from typing import List

def sort_array(array: List[int]) -> List[int]:
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    # Handle empty and single-element arrays
    if len(array) <= 1:
        return array[:] # Return a copy as required

    # Get first and last elements
    first_element = array[0]
    last_element = array[-1]

    # Calculate the sum and check if it's odd or even
    sum_first_last = first_element + last_element

    # Create a copy of the array for sorting
    copied_array = array[:]

    if sum_first_last % 2 != 0:  # Sum is odd
        copied_array.sort() # Sort in ascending order
    else:  # Sum is even
        copied_array.sort(reverse=True) # Sort in descending order

    return copied_array

class TestSortArray(unittest.TestCase):

    def test_empty_array(self):
        """Test with an empty input array."""
        self.assertEqual(sort_array([]), [])

    def test_single_element_array(self):
        """Test with an array containing a single element."""
        self.assertEqual(sort_array([5]), [5])
        self.assertEqual(sort_array([0]), [0])


    def test_sum_odd_ascending_sort(self):
        """Test cases where the sum of first and last is odd (ascending sort)."""
        # Example 3
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])
        # First=1, Last=2, Sum=3 (odd)
        self.assertEqual(sort_array([1, 3, 2]), [1, 2, 3])


    def test_sum_even_descending_sort(self):
        """Test cases where the sum of first and last is even (descending sort)."""
        # Example 4
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0])
        # First=1, Last=3, Sum=4 (even)
        self.assertEqual(sort_array([1, 2, 3]), [3, 2, 1])
        # First=0, Last=0, Sum=0 (even)
        self.assertEqual(sort_array([0, 0, 0]), [0, 0, 0])


    def test_sum_even_descending_sort_with_duplicates(self):
        """Test with sum even and duplicates."""
        # First=1, Last=1, Sum=2 (even)
        self.assertEqual(sort_array([1, 5, 1]), [5, 1, 1])
        # First=5, Last=5, Sum=10 (even)
        self.assertEqual(sort_array([5, 1, 5]), [5, 5, 1])


# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)