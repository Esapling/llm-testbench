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

if __name__ == "__main__":
    unittest.main()
