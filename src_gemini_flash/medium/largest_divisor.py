"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Iterate downwards from n // 2 to 1
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            return i
    # For prime numbers, the largest divisor smaller than n is 1.
    # The loop will reach i = 1 and return 1.

class TestLargestDivisor(unittest.TestCase):

    def test_example_case(self):
        """Test the example case from the docstring."""
        self.assertEqual(largest_divisor(15), 5)

    def test_prime_number(self):
        """Test with a prime number."""
        self.assertEqual(largest_divisor(7), 1)
        self.assertEqual(largest_divisor(2), 1) # Assuming n > 1 is handled

    def test_power_of_odd_prime(self):
        """Test with a number that is a power of an odd prime."""
        # 9 = 3^2, largest divisor < 9 is 3
        self.assertEqual(largest_divisor(9), 3)
        # 27 = 3^3, largest divisor < 27 is 9
        self.assertEqual(largest_divisor(27), 9)


    def test_power_of_even_prime(self):
        """Test with a number that is a power of 2."""
        # 8 = 2^3, largest divisor < 8 is 4
        self.assertEqual(largest_divisor(8), 4)
        # 16 = 2^4, largest divisor < 16 is 8
        self.assertEqual(largest_divisor(16), 8)


    def test_larger_composite_number(self):
        """Test with a larger composite number."""
        # 100 = 2^2 * 5^2, largest divisor < 100 is 50
        self.assertEqual(largest_divisor(100), 50)
        # 48 = 2^4 * 3, largest divisor < 48 is 24
        self.assertEqual(largest_divisor(48), 24)


# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)