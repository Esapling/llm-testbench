def derivative(xs: list):
    return [coeff * idx for idx, coeff in enumerate(xs)][1:]

import unittest

class TestDerivative(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])
    def test_example2(self):
        self.assertEqual(derivative([1, 2, 3]), [2, 6])