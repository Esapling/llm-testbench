import unittest


def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


class TestLargestPrimeFactor(unittest.TestCase):
    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)
        self.assertEqual(largest_prime_factor(13), 13)
        self.assertEqual(largest_prime_factor(100), 5)
        self.assertEqual(largest_prime_factor(121), 11)


if __name__ == '__main__':
    unittest.main()