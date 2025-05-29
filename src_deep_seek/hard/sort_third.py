"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def sort_third(l: list):
    """ Sort elements at indices divisible by 3 """
    indices = [i for i in range(len(l)) if i % 3 == 0]
    values = sorted([l[i] for i in indices])
    result = l.copy()
    for i, val in zip(indices, values):
        result[i] = val
    return result

class TestSortThird(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
    
    def test_example2(self):
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])
    
    def test_longer_list(self):
        self.assertEqual(sort_third([9, 1, 2, 3, 4, 5, 6, 7, 8]), [3, 1, 2, 6, 4, 5, 9, 7, 8])
    
    def test_empty_list(self):
        self.assertEqual(sort_third([]), [])

    # ----------- Phase 2 Tests -----------

    def test_sorted_in_divisible_by_three(self):
        self.assertEqual(sort_third([0, 1, 2, 3, 4, 5, 6]), [0, 1, 2, 3, 4, 5, 6]) 

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