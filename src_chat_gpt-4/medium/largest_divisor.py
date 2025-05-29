"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(n//2, 0, -1):
        if n % i == 0:
            return i

class Test(unittest.TestCase):
    def test_largest_divisor(self):
        self.assertEqual(largest_divisor(15), 5)
        self.assertEqual(largest_divisor(100), 50)
        self.assertEqual(largest_divisor(12), 6)
        self.assertEqual(largest_divisor(7), 1)
        
    # --------- Phase 2 Tests ---------
    
    def test_n_is_one(self):
        """ Test with n = 1, should return 0 or 1 based on the definition """
        self.assertEqual(largest_divisor(1), 0)

        
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
