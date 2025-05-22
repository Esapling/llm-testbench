"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def is_equal_to_sum_even(n):
    return n >= 8 and n % 2 == 0

class TestIsEqualToSumEven(unittest.TestCase):
    def test_examples(self):
        self.assertFalse(is_equal_to_sum_even(4))
        self.assertFalse(is_equal_to_sum_even(6))
        self.assertTrue(is_equal_to_sum_even(8))
        self.assertTrue(is_equal_to_sum_even(20))
        
    #---------- Phase 2 Tests ------------
    def test_odd_number(self):
        self.assertFalse(is_equal_to_sum_even(9))
    
    def test_negative_number(self):
        self.assertFalse(is_equal_to_sum_even(-4))
    
    def test_zero(self):
        self.assertFalse(is_equal_to_sum_even(0))
    
    def test_large_numbers(self):
        self.assertTrue(is_equal_to_sum_even(1000000))
        self.assertFalse(is_equal_to_sum_even(9999999))
        
    def test_non_integer(self):
        with self.assertRaises(TypeError):
            is_equal_to_sum_even("string")
        with self.assertRaises(TypeError):
            is_equal_to_sum_even(3.5)
            
    def test_floating_point(self):
        self.assertTrue(is_equal_to_sum_even(20.0))
        self.assertFalse(is_equal_to_sum_even(17.0))
        
        
if __name__ == "__main__":
    unittest.main()
