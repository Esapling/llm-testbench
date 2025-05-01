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
        self.assertEqual(sort_array([3, 1]), [1, 3])

if __name__ == "__main__":
    unittest.main()
