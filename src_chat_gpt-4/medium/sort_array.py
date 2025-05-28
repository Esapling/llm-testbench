"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def sort_array(array):
    """ Given an array of non-negative integers, return a sorted copy based on first and last value sum """
    if not array:
        return []
    
    if (array[0] + array[-1]) % 2 == 0:
        return sorted(array, reverse=True)
    return sorted(array)

class Test(unittest.TestCase):
    def test_sort_array(self):
        self.assertEqual(sort_array([5]), [5])
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0])
        self.assertEqual(sort_array([3, 1]), [3, 1])
    
    # --------- Phase 2 Tests ---------
    
    def test_empty_array(self):
        """ Test with an empty array, should return an empty array """
        self.assertEqual(sort_array([]), [])
        
    def test_large_numbers(self):
        """ Test with large numbers to ensure sorting works correctly """
        self.assertEqual(sort_array([100000000, 999999, 888888]), [100000000, 999999, 888888])
        self.assertEqual(sort_array([1000000, 5000000, 200000000]), [200000000, 5000000, 1000000])
    
    def test_original_array_unchanged(self):
        """ Ensure the original array is not modified """
        original = [2, 4, 3, 0, 1, 5]
        original_copy = original.copy()
        sorted_array = sort_array(original)
        self.assertEqual(original, original_copy)

if __name__ == "__main__":
    unittest.main()
