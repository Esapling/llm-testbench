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
    # Handle base cases
    if n == 0 or n == 1 or n == 3:
        return 0
    if n == 2:
        return 2
    
    # Initialize the first four values
    fib = [0, 0, 2, 0]
    
    # Compute values iteratively
    for i in range(4, n + 1):
        next_val = fib[0] + fib[1] + fib[2] + fib[3]
        # Shift the array (remove the oldest value and add the new one)
        fib = fib[1:] + [next_val]
    
    return fib[3]


# Unit tests
import unittest

class TestFib4(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(fib4(0), 0)
        self.assertEqual(fib4(1), 0)
        self.assertEqual(fib4(2), 2)
        self.assertEqual(fib4(3), 0)
    
    def test_example_cases(self):
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)
    
    def test_additional_cases(self):
        self.assertEqual(fib4(4), 2)  # 0 + 0 + 2 + 0 = 2
        self.assertEqual(fib4(8), 28)  # 0 + 2 + 4 + 8 = 14
        self.assertEqual(fib4(9), 52)  # 2 + 4 + 8 + 14 = 28
    
    def test_larger_values(self):
        self.assertEqual(fib4(10), 96)
        self.assertEqual(fib4(15), 5768)

if __name__ == "__main__":
    unittest.main()
