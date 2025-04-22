import math
import unittest
from typing import List

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    # The implementation correctly calculates the polynomial value
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

class TestPoly(unittest.TestCase):

    def test_quadratic_polynomial(self):
        """Test evaluation of a quadratic polynomial."""
        # Polynomial: x^2 - 2x + 1, coefficients [1, -2, 1]
        # At x = 5: 1*5^0 + (-2)*5^1 + 1*5^2 = 1 - 10 + 25 = 16
        self.assertEqual(poly([1, -2, 1], 5), 16)

    def test_evaluate_at_zero(self):
        """Test evaluation of a polynomial at x = 0."""
        # Polynomial: 5x^3 - 2.5x + 10, coefficients [10, -2.5, 0, 5]
        # At x = 0: 10*0^0 + (-2.5)*0^1 + 0*0^2 + 5*0^3 = 10
        self.assertEqual(poly([10, -2.5, 0, 5], 0), 10)

    def test_evaluate_at_one(self):
        """Test evaluation of a polynomial at x = 1."""
        # Polynomial: 3x^2 + 2x + 1, coefficients [1, 2, 3]
        # At x = 1: 1*1^0 + 2*1^1 + 3*1^2 = 1 + 2 + 3 = 6
        self.assertEqual(poly([1, 2, 3], 1), 6)

    def test_empty_coefficients(self):
        """Test evaluation with an empty list of coefficients."""
        # Represents a polynomial of degree -1 or no polynomial.
        # The sum of an empty list is 0.
        self.assertEqual(poly([], 2), 0)
        self.assertEqual(poly([], 0), 0)

    def test_non_integer_x(self):
        """Test evaluation with a non-integer value for x."""
        # Polynomial: x^2, coefficients [0, 0, 1]
        # At x = 2.5: 0*2.5^0 + 0*2.5^1 + 1*2.5^2 = 6.25
        self.assertEqual(poly([0, 0, 1], 2.5), 6.25)

# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)