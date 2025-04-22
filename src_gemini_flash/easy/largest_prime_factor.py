import unittest
import math

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_factor = 1

    # Handle factor 2
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    # Handle odd factors
    # We only need to check up to the square root of the remaining n
    # We can step by 2 since we've handled all factors of 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            largest_factor = i
            n //= i

    # If n is still greater than 1, the remaining n is prime and is the largest factor
    if n > 1:
        largest_factor = n

    return largest_factor

class TestLargestPrimeFactor(unittest.TestCase):

    def test_example_1(self):
        """Test the first example case."""
        self.assertEqual(largest_prime_factor(13195), 29)

    def test_example_2_power_of_prime(self):
        """Test the second example case (power of 2)."""
        self.assertEqual(largest_prime_factor(2048), 2)

    def test_small_distinct_prime_factors(self):
        """Test a number with small distinct prime factors."""
        # 100 = 2^2 * 5^2
        self.assertEqual(largest_prime_factor(100), 5)
        # 42 = 2 * 3 * 7
        self.assertEqual(largest_prime_factor(42), 7)

    def test_larger_prime_factor(self):
        """Test a number with a larger prime factor."""
        # 999 = 3^3 * 37
        self.assertEqual(largest_prime_factor(999), 37)
        # 143 = 11 * 13
        self.assertEqual(largest_prime_factor(143), 13)


    def test_product_of_two_primes(self):
        """Test a number that is a product of two primes."""
        # 17 * 19 = 323
        self.assertEqual(largest_prime_factor(323), 19)
        # 5 * 7 = 35
        self.assertEqual(largest_prime_factor(35), 7)


# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)