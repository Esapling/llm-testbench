import unittest

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n"""
    if n <= 1:
        return 0
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
    return 1

class TestLargestDivisor(unittest.TestCase):
    def test_example(self):
        self.assertEqual(largest_divisor(15), 5)
    
    def test_prime(self):
        self.assertEqual(largest_divisor(17), 1)
    
    def test_square_number(self):
        self.assertEqual(largest_divisor(16), 8)
    
    def test_small_number(self):
        self.assertEqual(largest_divisor(2), 1)
    
    def test_one(self):
        self.assertEqual(largest_divisor(1), 0)

if __name__ == "__main__":
    unittest.main()