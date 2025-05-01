"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import math
import unittest

def poly(xs: list, x: float):
    """Evaluate polynomial at x."""
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """Find a zero point of the polynomial with given coefficients."""
    low, high = -1e5, 1e5
    while high - low > 1e-7:
        mid = (low + high) / 2
        if poly(xs, mid) * poly(xs, low) <= 0:
            high = mid
        else:
            low = mid
    return (low + high) / 2

class Test(unittest.TestCase):
    def test_linear(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=2)
    def test_cubic(self):
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=2)
    def test_simple(self):
        self.assertAlmostEqual(find_zero([1, -1]), 1.0, places=2)

if __name__ == "__main__":
    unittest.main()
