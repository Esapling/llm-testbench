"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def largest_prime_factor(n: int) -> int:
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n

class TestLargestPrimeFactor(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)

    def test_small_numbers(self):
        self.assertEqual(largest_prime_factor(6), 3)
        self.assertEqual(largest_prime_factor(15), 5)

if __name__ == "__main__":
    unittest.main()
