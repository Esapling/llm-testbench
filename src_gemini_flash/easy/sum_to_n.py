import unittest


def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """

    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")

    return n * (n + 1) // 2


class TestSumToN(unittest.TestCase):
    def test_sum_to_n(self):
        self.assertEqual(sum_to_n(30), 465)
        self.assertEqual(sum_to_n(100), 5050)
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(10), 55)
        self.assertEqual(sum_to_n(1), 1)
        self.assertEqual(sum_to_n(0), 0)
        with self.assertRaises(ValueError):
            sum_to_n(-1)
        with self.assertRaises(ValueError):
            sum_to_n(1.5)


if __name__ == '__main__':
    unittest.main()