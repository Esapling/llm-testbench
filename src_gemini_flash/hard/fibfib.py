"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
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

    # Initialize with the first two terms
    a, b = 0, 1 # a is F(i-2), b is F(i-1) in the loop

    # Calculate subsequent terms iteratively
    for _ in range(2, n + 1):
        # The next term is the product of the previous two
        # In the next iteration, the current b becomes the new a
        # and the calculated next_fibfib becomes the new b
        next_fibfib = a * b
        a = b
        b = next_fibfib

    return b

class TestFibFib(unittest.TestCase):

    def test_fibfib_base_cases(self):
        """Test the base cases F(0) and F(1)."""
        self.assertEqual(fibfib(0), 0)
        self.assertEqual(fibfib(1), 1)

    def test_fibfib_n_equals_2_and_3(self):
        """Test fibfib for n=2 and n=3, where the product rule starts."""
        self.assertEqual(fibfib(2), 0)
        self.assertEqual(fibfib(3), 0)

    def test_fibfib_larger_n_are_zero(self):
        """Test that fibfib is 0 for n >= 2."""
        self.assertEqual(fibfib(4), 0)
        self.assertEqual(fibfib(5), 0)
        self.assertEqual(fibfib(10), 0)


    def test_fibfib_negative_input(self):
        """Test that a ValueError is raised for negative input."""
        with self.assertRaises(ValueError):
            fibfib(-1)
        with self.assertRaises(ValueError):
            fibfib(-5)

    # -------------- Phase 2 Tests -------------
    
    def test_n_greater_than_3(self):
        self.assertEqual(fibfib(4), 2)
        self.assertEqual(fibfib(6), 7)
        self.assertEqual(fibfib(10), 44)
    
    def test_large_n(self):
        self.assertEqual(fibfib(20), 17711)
    
    def test_non_integer_n(self):
        with self.assertRaises(TypeError):
            fibfib(5.5)
        with self.assertRaises(TypeError):
            fibfib("string")
        with self.assertRaises(TypeError):
            fibfib([1, 2, 3])
        with self.assertRaises(TypeError):
            fibfib(None)


# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)