"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # The smallest possible sum of 4 positive even numbers is 2+2+2+2 = 8
    if n < 8:
        return False
    
    # If n is odd, it can't be a sum of even numbers
    if n % 2 != 0:
        return False
    
    # Every even number >= 8 can be represented as 2+2+2+(n-6)
    # where (n-6) is also even and positive
    return True


# Unit tests
import unittest

class TestIsEqualToSumEven(unittest.TestCase):
    def test_example_case_1(self):
        self.assertFalse(is_equal_to_sum_even(4))
    
    def test_example_case_2(self):
        self.assertFalse(is_equal_to_sum_even(6))
    
    def test_example_case_3(self):
        self.assertTrue(is_equal_to_sum_even(8))
    
    def test_minimum_valid_value(self):
        self.assertTrue(is_equal_to_sum_even(8))  # 2+2+2+2
    
    def test_larger_valid_values(self):
        self.assertTrue(is_equal_to_sum_even(10))  # 2+2+2+4
        self.assertTrue(is_equal_to_sum_even(12))  # 2+2+4+4
        self.assertTrue(is_equal_to_sum_even(20))  # 2+2+6+10
    
    def test_odd_values(self):
        self.assertFalse(is_equal_to_sum_even(9))
        self.assertFalse(is_equal_to_sum_even(11))
        self.assertFalse(is_equal_to_sum_even(15))
    
    def test_zero(self):
        self.assertFalse(is_equal_to_sum_even(0))  # We need positive even numbers
    
    def test_negative(self):
        self.assertFalse(is_equal_to_sum_even(-4))  # We need positive numbers

        #---------- Phase 2 Tests ------------
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
