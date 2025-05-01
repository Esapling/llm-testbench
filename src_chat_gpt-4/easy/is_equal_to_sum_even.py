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

if __name__ == "__main__":
    unittest.main()
