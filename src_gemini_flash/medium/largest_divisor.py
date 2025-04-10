import unittest


def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            return i


class TestLargestDivisor(unittest.TestCase):
    def test_largest_divisor(self):
        self.assertEqual(largest_divisor(15), 5)
        self.assertEqual(largest_divisor(10), 5)
        self.assertEqual(largest_divisor(13), 1)
        self.assertEqual(largest_divisor(20), 10)
        self.assertEqual(largest_divisor(2), 1)


if __name__ == '__main__':
    unittest.main()