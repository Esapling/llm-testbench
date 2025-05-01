"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import math
import unittest

def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_factor = 1
    # Handle 2 separately
    while n % 2 == 0:
        largest_factor = 2
        n = n // 2
    # Check odd divisors up to sqrt(n)
    i = 3
    max_factor = math.isqrt(n) + 1
    while i <= max_factor:
        while n % i == 0:
            largest_factor = i
            n = n // i
            max_factor = math.isqrt(n) + 1
        i += 2
    if n > 1:
        largest_factor = n
    return largest_factor

class TestLargestPrimeFactor(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(largest_prime_factor(13195), 29)
    
    def test_example2(self):
        self.assertEqual(largest_prime_factor(2048), 2)
    
    def test_small_composite(self):
        self.assertEqual(largest_prime_factor(15), 5)
    
    def test_product_of_primes(self):
        self.assertEqual(largest_prime_factor(17*19), 19)
    
    def test_product_of_multiple_primes(self):
        self.assertEqual(largest_prime_factor(2*3*5*7), 7)

if __name__ == "__main__":
    unittest.main()