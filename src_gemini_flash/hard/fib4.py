import unittest


def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """

    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n <= 3:
        return [0, 0, 2, 0][n]

    seq = [0, 0, 2, 0]
    for i in range(4, n + 1):
        next_fib = seq[i - 1] + seq[i - 2] + seq[i - 3] + seq[i - 4]
        seq.append(next_fib)

    return seq[n]


class TestFib4(unittest.TestCase):
    def test_fib4(self):
        self.assertEqual(fib4(0), 0)
        self.assertEqual(fib4(1), 0)
        self.assertEqual(fib4(2), 2)
        self.assertEqual(fib4(3), 0)
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)
        self.assertEqual(fib4(10), 54)
        self.assertEqual(fib4(15), 1044)
        with self.assertRaises(ValueError):
            fib4(-1)


if __name__ == '__main__':
    unittest.main()