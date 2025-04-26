import unittest

def is_equal_to_sum_even(n: int) -> bool:
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers"""
    return n >= 8 and n % 2 == 0

class TestIsEqualToSumEven(unittest.TestCase):
    def test_example1(self):
        self.assertFalse(is_equal_to_sum_even(4))
    
    def test_example2(self):
        self.assertFalse(is_equal_to_sum_even(6))
    
    def test_example3(self):
        self.assertTrue(is_equal_to_sum_even(8))
    
    def test_larger_number(self):
        self.assertTrue(is_equal_to_sum_even(10))
    
    def test_odd_number(self):
        self.assertFalse(is_equal_to_sum_even(7))

if __name__ == "__main__":
    unittest.main()