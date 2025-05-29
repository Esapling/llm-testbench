"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n"""
    if n <= 1:
        return 0
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
    return 1

class TestLargestDivisor(unittest.TestCase):
    def test_example(self):
        self.assertEqual(largest_divisor(15), 5)
    
    def test_prime(self):
        self.assertEqual(largest_divisor(17), 1)
    
    def test_square_number(self):
        self.assertEqual(largest_divisor(16), 8)
    
    def test_small_number(self):
        self.assertEqual(largest_divisor(2), 1)
    
    def test_one(self):
        self.assertEqual(largest_divisor(1), 0)

# --------- Phase 2 Tests ---------
        
    def test_negative_number(self):
        """ Test with a negative number, should return 0 or raise an error """
        with self.assertRaises(ValueError):
            largest_divisor(-10)
    
    def test_zero(self):
        """ Test with n = 0, should return 0 or raise an error """
        with self.assertRaises(ValueError):
            largest_divisor(0)
            
    '''
    def test_large_number(self):
        """ Test with a large number to check performance """
        self.assertEqual(largest_divisor(1000000), 500000)
        self.assertEqual(largest_divisor(999999999), 333333333)
    '''     
    
    def test_non_integer_input(self):
        """ Test with non-integer input, should raise an error """
        with self.assertRaises(TypeError):
            largest_divisor(15.5)
        with self.assertRaises(TypeError):
            largest_divisor("fifteen")
            
if __name__ == "__main__":
    unittest.main()