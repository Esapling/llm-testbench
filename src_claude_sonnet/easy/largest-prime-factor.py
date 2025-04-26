def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Start with the smallest prime factor, 2
    i = 2
    
    # Keep dividing n by its factors until we reach the largest one
    while i * i <= n:
        if n % i:
            # If i is not a factor of n, try the next number
            i += 1
        else:
            # If i is a factor of n, divide n by i and continue
            n //= i
    
    # The remaining n is the largest prime factor
    return n


# Unit tests
import unittest

class TestLargestPrimeFactor(unittest.TestCase):
    def test_example_case_1(self):
        self.assertEqual(largest_prime_factor(13195), 29)
    
    def test_example_case_2(self):
        self.assertEqual(largest_prime_factor(2048), 2)
    
    def test_large_number(self):
        self.assertEqual(largest_prime_factor(600851475143), 6857)
    
    def test_power_of_prime(self):
        self.assertEqual(largest_prime_factor(128), 2)  # 2^7
    
    def test_product_of_primes(self):
        self.assertEqual(largest_prime_factor(2 * 3 * 5 * 7 * 11), 11)
    
    def test_small_composite(self):
        self.assertEqual(largest_prime_factor(10), 5)  # 2 * 5

if __name__ == "__main__":
    unittest.main()
