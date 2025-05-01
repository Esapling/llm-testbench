"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def fib4(n: int):
    """Compute the n-th element of the fib4 sequence."""
    a, b, c, d = 0, 0, 2, 0
    if n == 0:
        return a
    elif n == 1:
        return b
    elif n == 2:
        return c
    elif n == 3:
        return d
    for _ in range(4, n + 1):
        a, b, c, d = b, c, d, a + b + c + d
    return d

class Test(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(fib4(5), 4)
    def test_example(self):
        self.assertEqual(fib4(6), 8)
    def test_edge(self):
        self.assertEqual(fib4(7), 14)
    def test_zero(self):
        self.assertEqual(fib4(0), 0)

if __name__ == "__main__":
    unittest.main()
