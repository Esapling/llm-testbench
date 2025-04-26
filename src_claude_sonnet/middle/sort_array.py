def sort_array(array):
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
    # Handle empty array or single element array
    if len(array) <= 1:
        return array.copy()
    
    # Calculate sum of first and last elements
    sum_first_last = array[0] + array[-1]
    
    # Create a copy of the array
    result = array.copy()
    
    # Sort based on sum
    if sum_first_last % 2 == 1:  # Odd sum
        result.sort()  # Ascending order
    else:  # Even sum
        result.sort(reverse=True)  # Descending order
    
    return result

import unittest

class TestSortArray(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sort_array([]), [])
        self.assertEqual(sort_array([5]), [5])
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0])
        
    def test_odd_sum(self):
        self.assertEqual(sort_array([3, 1, 2, 4]), [1, 2, 3, 4])  # 3+4=7, odd
        self.assertEqual(sort_array([5, 4, 3, 2, 1, 0]), [0, 1, 2, 3, 4, 5])  # 5+0=5, odd
        
    def test_even_sum(self):
        self.assertEqual(sort_array([2, 3, 4, 6]), [6, 4, 3, 2])  # 2+6=8, even
        self.assertEqual(sort_array([6, 5, 4, 3, 2, 8]), [8, 6, 5, 4, 3, 2])  # 6+8=14, even
        
    def test_original_array_unchanged(self):
        original = [2, 4, 3, 0, 1, 5]
        original_copy = original.copy()
        sort_array(original)
        self.assertEqual(original, original_copy)

if __name__ == "__main__":
    unittest.main()
