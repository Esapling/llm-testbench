import unittest

def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.
    """
    if not array:
        return array.copy()
    first, last = array[0], array[-1]
    sorted_arr = array.copy()
    if (first + last) % 2 == 1:
        sorted_arr.sort()
    else:
        sorted_arr.sort(reverse=True)
    return sorted_arr

class TestSortArray(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(sort_array([]), [])
    
    def test_single(self):
        self.assertEqual(sort_array([5]), [5])
    
    def test_odd_sum(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])
    
    def test_even_sum(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0])
    
    def test_no_modification(self):
        arr = [3, 1, 2]
        sorted_arr = sort_array(arr)
        self.assertEqual(arr, [3, 1, 2])
        self.assertIsNot(arr, sorted_arr)

if __name__ == "__main__":
    unittest.main()