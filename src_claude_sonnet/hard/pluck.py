"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes
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
    if not arr:
        return []
    
    min_even_value = float('inf')
    min_even_index = -1
    
    for i, value in enumerate(arr):
        # Check if the value is even and smaller than current minimum
        if value % 2 == 0 and value < min_even_value:
            min_even_value = value
            min_even_index = i
    
    # If no even value found
    if min_even_index == -1:
        return []
    
    return [min_even_value, min_even_index]


# Unit tests
import unittest

class TestPluck(unittest.TestCase):
    def test_example_case_1(self):
        self.assertEqual(pluck([4, 2, 3]), [2, 1])
    
    def test_example_case_2(self):
        self.assertEqual(pluck([1, 2, 3]), [2, 1])
    
    def test_example_case_3(self):
        self.assertEqual(pluck([]), [])
    
    def test_example_case_4(self):
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])
    
    def test_no_even_values(self):
        self.assertEqual(pluck([1, 3, 5, 7, 9]), [])
    
    def test_all_even_values(self):
        self.assertEqual(pluck([8, 6, 4, 2, 0]), [0, 4])
    
    def test_single_element_even(self):
        self.assertEqual(pluck([2]), [2, 0])
    
    def test_single_element_odd(self):
        self.assertEqual(pluck([3]), [])
    
    def test_larger_array(self):
        self.assertEqual(pluck([101, 99, 51, 8, 24, 36, 2, 3, 5, 7, 2]), [2, 6])

if __name__ == "__main__":
    unittest.main()
