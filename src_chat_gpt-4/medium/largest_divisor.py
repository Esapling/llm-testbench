import unittest

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(n//2, 0, -1):
        if n % i == 0:
            return i

class Test(unittest.TestCase):
    def test_largest_divisor(self):
        self.assertEqual(largest_divisor(15), 5)
        self.assertEqual(largest_divisor(100), 50)
        self.assertEqual(largest_divisor(12), 6)
        self.assertEqual(largest_divisor(7), 1)

if __name__ == "__main__":
    unittest.main()
