"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence. Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    # Use an iterative approach to calculate fib4(n)
    # We need to keep track of the last four values: fib4(n-1), fib4(n-2), fib4(n-3), fib4(n-4)
    a, b, c, d = 0, 0, 2, 0  # Initialize with fib4(0), fib4(1), fib4(2), fib4(3)

    for i in range(4, n + 1):
        next_fib4 = a + b + c + d
        # Shift the values
        a = b
        b = c
        c = d
        d = next_fib4

    return d

class TestFib4(unittest.TestCase):

    def test_fib4_base_cases(self):
        """Test the base cases of the fib4 sequence."""
        self.assertEqual(fib4(0), 0)
        self.assertEqual(fib4(1), 0)
        self.assertEqual(fib4(2), 2)
        self.assertEqual(fib4(3), 0)

    def test_fib4_example_cases(self):
        """Test the example cases provided in the docstring."""
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)

    def test_fib4_n_is_4(self):
        """Test the value of fib4(4)."""
        # fib4(4) = fib4(3) + fib4(2) + fib4(1) + fib4(0) = 0 + 2 + 0 + 0 = 2
        self.assertEqual(fib4(4), 2)

    def test_fib4_larger_n(self):
        """Test fib4 for a slightly larger value."""
        # fib4(8) = fib4(7) + fib4(6) + fib4(5) + fib4(4) = 14 + 8 + 4 + 2 = 28
        self.assertEqual(fib4(8), 28)

    def test_fib4_n_is_10(self):
        """Test fib4 for n=10."""
        # fib4(0)=0, fib4(1)=0, fib4(2)=2, fib4(3)=0
        # fib4(4) = 0+0+2+0 = 2
        # fib4(5) = 0+2+0+2 = 4
        # fib4(6) = 2+0+2+4 = 8
        # fib4(7) = 0+2+4+8 = 14
        # fib4(8) = 2+4+8+14 = 28
        # fib4(9) = 4+8+14+28 = 54
        # fib4(10) = 8+14+28+54 = 104
        self.assertEqual(fib4(10), 104)

# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)