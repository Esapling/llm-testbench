"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def pluck(arr):
    """Pluck the smallest even value from the list."""
    even_vals = [(val, idx) for idx, val in enumerate(arr) if val % 2 == 0]
    if not even_vals:
        return []
    return list(min(even_vals, key=lambda x: (x[0], x[1])))

class Test(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(pluck([4, 2, 3]), [2, 1])
    def test_with_zero(self):
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])
    def test_no_even(self):
        self.assertEqual(pluck([1, 3, 5]), [])
    def test_empty(self):
        self.assertEqual(pluck([]), [])
        
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
