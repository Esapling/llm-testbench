import unittest


def fibfib(n):
    """
    The FibFibonacci sequence is defined as follows:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) * F(n-2) for n > 1
    Given a number n, find the nth element of the FibFibonacci sequence.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a * b
    return b


class TestFibFib(unittest.TestCase):
    def test_fibfib(self):
        self.assertEqual(fibfib(0), 0)
        self.assertEqual(fibfib(1), 1)
        self.assertEqual(fibfib(2), 1)
        self.assertEqual(fibfib(3), 1)
        self.assertEqual(fibfib(4), 2)
        self.assertEqual(fibfib(5), 2)
        self.assertEqual(fibfib(6), 4)
        self.assertEqual(fibfib(7), 8)
        self.assertEqual(fibfib(8), 32)
        with self.assertRaises(ValueError):
            fibfib(-1)


if __name__ == '__main__':
    unittest.main()