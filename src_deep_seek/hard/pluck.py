"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def pluck(arr):
    """ Find and return the smallest even value with its index """
    if not arr:
        return []
    
    min_even = None
    min_index = -1
    
    for i, num in enumerate(arr):
        if num % 2 == 0:
            if min_even is None or num < min_even:
                min_even = num
                min_index = i
    
    return [min_even, min_index] if min_even is not None else []

class TestPluck(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(pluck([4, 2, 3]), [2, 1])
    
    def test_example2(self):
        self.assertEqual(pluck([1, 2, 3]), [2, 1])
    
    def test_example3(self):
        self.assertEqual(pluck([]), [])
    
    def test_example4(self):
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])
    
    def test_no_evens(self):
        self.assertEqual(pluck([1, 3, 5]), [])

    # ---------- Phase 2 Tests ----------

    def test_all_even_numbers(self):
        self.assertEqual(pluck([4, 2, 6, 8]), [2, 1])
        
    def test_single_even(self):
        self.assertEqual(pluck([2]), [2, 0])
        
    def test_single_odd(self):
        self.assertEqual(pluck([3]), [])

    def test_large_numbers(self):
        self.assertEqual(pluck([100000000, 5000000, 200000000]), [5000000, 1])

    def test_strings_in_list(self):
        with self.assertRaises(TypeError):
            pluck([1, 'two', 3])
            

if __name__ == "__main__":
    unittest.main()