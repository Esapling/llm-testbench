"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def fibfib(n: int):
    """Compute the n-th element of the fibfib sequence."""
    a, b, c = 0, 0, 1
    if n == 0:
        return a
    elif n == 1:
        return b
    elif n == 2:
        return c
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c

class Test(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(fibfib(1), 0)
    def test_example(self):
        self.assertEqual(fibfib(5), 4)
    def test_large(self):
        self.assertEqual(fibfib(8), 24)
    def test_zero(self):
        self.assertEqual(fibfib(0), 0)

if __name__ == "__main__":
    unittest.main()
