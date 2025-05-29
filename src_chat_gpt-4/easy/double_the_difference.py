"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def double_the_difference(lst):
    return sum(x**2 for x in lst if isinstance(x, int) and x > 0 and x % 2 == 1)

class TestDoubleTheDifference(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)
        self.assertEqual(double_the_difference([9, -2]), 81)
        self.assertEqual(double_the_difference([0]), 0)
        
    #------------ Phase 2 Tests ------------
    
    def test_empty_list(self):
        self.assertEqual(double_the_difference([]), 0)
    
    def test_mixed_types(self):
        self.assertEqual(double_the_difference([1, 2, 3.5, 4, 5, -7, 0]), 26)
    
    def test_only_even_and_negative(self):
        self.assertEqual(double_the_difference([2, 4, -6, -8, 0]), 0)

    def test_with_strings(self):
        self.assertEqual(double_the_difference([1, 'a', 3, 4]), 10)
    
    def test_boolean_inputs(self):
        self.assertRaises(TypeError, double_the_difference, [True, False, 1])

if __name__ == "__main__":
    unittest.main()
