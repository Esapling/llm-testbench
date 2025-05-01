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

if __name__ == "__main__":
    unittest.main()