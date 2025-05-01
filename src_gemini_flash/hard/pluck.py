"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest
from typing import List, Optional

def pluck(arr: List[int]) -> List[int]:
    """Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smalest_value, its index ],
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 3:
        Input: []
        Output: []

    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
        Explanation: 0 is the smallest value, but  there are two zeros,
                     so we will choose the first zero, which has the smallest index.

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    """
    smallest_even_value = float('inf')
    smallest_even_index = -1

    for index, value in enumerate(arr):
        if value % 2 == 0:
            if value < smallest_even_value:
                smallest_even_value = value
                smallest_even_index = index
            # The requirement is to return the one with the smallest index if values are equal.
            # However, the current logic finds the first occurrence of the smallest even value
            # because we only update when a strictly smaller value is found.
            # If an equal value is found later, its index will be larger, so we don't update.
            # This satisfies the "smallest index" requirement implicitly when finding the minimum value.
            # If there were multiple occurrences of the *true* smallest even value,
            # the loop finds the first one due to the iteration order.

    if smallest_even_value == float('inf'):
        return []
    else:
        return [int(smallest_even_value), smallest_even_index]

class TestPluck(unittest.TestCase):

    def test_example_1(self):
        """Test example 1 from the docstring."""
        self.assertEqual(pluck([4, 2, 3]), [2, 1])

    def test_example_3_empty_array(self):
        """Test with an empty input array."""
        self.assertEqual(pluck([]), [])

    def test_example_4_smallest_even_zero(self):
        """Test example 4 with 0 as the smallest even number."""
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

    def test_only_odd_numbers(self):
        """Test with an array containing only odd numbers."""
        self.assertEqual(pluck([1, 3, 5, 7]), [])

    def test_smallest_even_at_the_end(self):
        """Test when the smallest even number is the last element."""
        self.assertEqual(pluck([8, 6, 4, 2]), [2, 3])

# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)