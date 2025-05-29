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
        
        #--------------Phase 2 Tests--------------
        
    def test_smallest_non_prime(self):
        self.assertEqual(largest_prime_factor(4), 2)

    def test_large_number(self):
        self.assertEqual(largest_prime_factor(600851475143), 6857)
        
    def test_floating_point(self):
        self.assertTrue(largest_prime_factor(20.0))

if __name__ == "__main__":
    unittest.main()

