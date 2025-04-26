import math

def poly(xs: list, x: float):
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def find_zero(xs: list):
    left, right = -1e6, 1e6
    while right - left > 1e-7:
        mid = (left + right) / 2
        if poly(xs, mid) * poly(xs, left) <= 0:
            right = mid
        else:
            left = mid
    return (left + right) / 2

import unittest

class TestFindZero(unittest.TestCase):
    def test_linear(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=2)
    def test_cubic(self):
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=2)