"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
def largest_divisor(n: int) -> int:
    """For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Start checking from n//2 since that's the largest possible divisor smaller than n
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            return i
    return 1  # Default case if n is 1 or prime

import unittest

class TestLargestDivisor(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(largest_divisor(15), 5)
        
    def test_prime_number(self):
        self.assertEqual(largest_divisor(7), 1)
        
    def test_even_number(self):
        self.assertEqual(largest_divisor(16), 8)
        
    def test_number_one(self):
        self.assertEqual(largest_divisor(1), 1)
        
    def test_large_number(self):
        self.assertEqual(largest_divisor(100), 50)
        
    def test_composite_number(self):
        self.assertEqual(largest_divisor(24), 12)

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
