"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def derivative(xs: list):
    """Compute the derivative of a polynomial."""
    return [i * xs[i] for i in range(1, len(xs))]

class Test(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])
    def test_quadratic(self):
        self.assertEqual(derivative([1, 2, 3]), [2, 6])
    def test_linear(self):
        self.assertEqual(derivative([5, 7]), [7])
    def test_constant(self):
        self.assertEqual(derivative([3]), [])

if __name__ == "__main__":
    unittest.main()
