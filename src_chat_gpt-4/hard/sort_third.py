"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def sort_third(l: list):
    """Sort elements at indices divisible by 3, keep others in place."""
    sorted_third = sorted([l[i] for i in range(len(l)) if i % 3 == 0])
    result = l[:]
    j = 0
    for i in range(len(l)):
        if i % 3 == 0:
            result[i] = sorted_third[j]
            j += 1
    return result

class Test(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
    def test_with_non_divisible(self):
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])
    def test_empty(self):
        self.assertEqual(sort_third([]), [])
    def test_large_list(self):
        self.assertEqual(sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    # ----------- Phase 2 Tests -----------
    
    def test_one_divisible_by_three(self):
        self.assertEqual(sort_third([30, 20, 40]), [30, 20, 40])
        self.assertEqual(sort_third([1, 2]), [1, 2])
    
    def test_sorted_in_divisible_by_three(self):
        self.assertEqual(sort_third([0, 1, 2, 3, 4, 5, 6]), [0, 1, 2, 3, 4, 5, 6]) 
    
    def test_unsorted_divisible_by_three(self):
        self.assertEqual(sort_third([6, 5, 4, 3, 2, 1, 0]), [0, 5, 4, 3, 2, 1, 6])
        self.assertEqual(sort_third([9, 8, 7, 15, 5, 4, 3, 2, 1, 12]), [3, 8, 7, 9, 5, 4, 12, 2, 1, 15])

    def test_negative_numbers(self):
        self.assertEqual(sort_third([-1, -2, -3, -4, -5, -6]), [-4, -2, -3, -1, -5, -6])
        self.assertEqual(sort_third([-10, -20, -30]), [-10, -20, -30])
        
    def test_large_numbers(self):
        self.assertEqual(sort_third([999999999, 888888888, 777777777, 0]), [0, 888888888, 777777777, 999999999])
        
    def test_strings_and_numbers(self):
        with self.assertRaises(TypeError):
            sort_third([1, 'a', 3, 'b', 5, 'c'])
        
if __name__ == "__main__":
    unittest.main()
