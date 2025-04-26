import math
import unittest

def poly(xs: list, x: float):
    """ Evaluates polynomial with coefficients xs at point x """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ Find x such that poly(x) = 0 """
    if len(xs) % 2 != 0:
        raise ValueError("Number of coefficients must be even")
    
    # Using binary search between -1000 and 1000
    left, right = -1000, 1000
    for _ in range(100):
        mid = (left + right) / 2
        val = poly(xs, mid)
        if abs(val) < 1e-9:
            return mid
        if val * poly(xs, left) < 0:
            right = mid
        else:
            left = mid
    return (left + right) / 2

class TestFindZero(unittest.TestCase):
    def test_example1(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=2)
    
    def test_example2(self):
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=2)
    
    def test_quadratic(self):
        self.assertAlmostEqual(find_zero([-4, 0, 1]), 2.0, places=2)
    
    def test_odd_coefficients(self):
        with self.assertRaises(ValueError):
            find_zero([1, 2, 3])

if __name__ == "__main__":
    unittest.main()