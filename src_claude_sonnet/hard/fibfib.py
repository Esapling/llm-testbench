"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def fibfib(n: int) -> int:
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    # For n >= 3, use iterative approach to avoid recursion
    a, b, c = 0, 0, 1  # fibfib(0), fibfib(1), fibfib(2)
    
    for i in range(3, n + 1):
        next_val = a + b + c
        a, b, c = b, c, next_val
    
    return c

class TestFibFib(unittest.TestCase):
    
    def test_base_cases(self):
        """Test the base cases of the FibFib sequence."""
        self.assertEqual(fibfib(0), 0)
        self.assertEqual(fibfib(1), 0)
        self.assertEqual(fibfib(2), 1)
    
    def test_small_values(self):
        """Test some small values against known results."""
        self.assertEqual(fibfib(3), 1)  # 0 + 0 + 1 = 1
        self.assertEqual(fibfib(4), 2)  # 1 + 0 + 1 = 2
        self.assertEqual(fibfib(5), 4)  # 2 + 1 + 1 = 4
        self.assertEqual(fibfib(6), 7)  # 4 + 2 + 1 = 7
        self.assertEqual(fibfib(7), 13) # 7 + 4 + 2 = 13
        self.assertEqual(fibfib(8), 24) # 13 + 7 + 4 = 24
    
    def test_larger_values(self):
        """Test some larger values of the sequence."""
        self.assertEqual(fibfib(10), 81)
        self.assertEqual(fibfib(15), 1705)
    
    def test_sequence_relation(self):
        """Test that the recursive relation holds for some values."""
        n = 9
        self.assertEqual(fibfib(n), fibfib(n-1) + fibfib(n-2) + fibfib(n-3))
        
        n = 12
        self.assertEqual(fibfib(n), fibfib(n-1) + fibfib(n-2) + fibfib(n-3))
    
    def test_negative_input(self):
        """Test that the function raises an error for negative inputs."""
        with self.assertRaises(ValueError):
            fibfib(-1)

    # -------------- Phase 2 Tests -------------

    def test_non_integer_n(self):
        with self.assertRaises(TypeError):
            fibfib(5.5)
        with self.assertRaises(TypeError):
            fibfib("string")
        with self.assertRaises(TypeError):
            fibfib([1, 2, 3])
        with self.assertRaises(TypeError):
            fibfib(None)

if __name__ == '__main__':
    unittest.main()