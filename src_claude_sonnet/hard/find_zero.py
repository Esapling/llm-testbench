"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # We'll use the bisection method to find a zero of the polynomial
    # First, we need to find an interval [a, b] where f(a) and f(b) have opposite signs
    
    # Start with a reasonable interval
    a, b = -10.0, 10.0
    
    # Ensure we have opposite signs
    while poly(xs, a) * poly(xs, b) > 0:
        a *= 2
        b *= 2
    
    # Apply bisection method until we get close enough
    epsilon = 1e-10  # Desired precision
    
    while (b - a) > epsilon:
        c = (a + b) / 2.0  # Midpoint
        
        if abs(poly(xs, c)) < epsilon:
            # Found a close enough solution
            return c
        
        if poly(xs, a) * poly(xs, c) < 0:
            # Root is in [a, c]
            b = c
        else:
            # Root is in [c, b]
            a = c
    
    # Return the midpoint of the final interval
    return (a + b) / 2.0


# Unit tests
import unittest

class TestFindZero(unittest.TestCase):
    def test_example_case_1(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=2)
    
    def test_example_case_2(self):
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=2)
    
    def test_quadratic(self):
        # x^2 - 4 = 0 => x = 2 or x = -2, should return one of them
        result = find_zero([-4, 0, 1])
        self.assertTrue(abs(abs(result) - 2.0) < 1e-5)
    
    def test_cubic(self):
        # x^3 - x = 0 => x = 0, x = 1, x = -1, should return one of them
        result = find_zero([0, -1, 0, 1])
        self.assertTrue(abs(result) < 1e-5 or abs(abs(result) - 1.0) < 1e-5)
    
    def test_higher_degree(self):
        # x^4 - 16 = 0 => x = 2, x = -2, x = 2i, x = -2i, should return 2 or -2
        result = find_zero([-16, 0, 0, 0, 1])
        self.assertTrue(abs(abs(result) - 2.0) < 1e-5)

if __name__ == "__main__":
    unittest.main()
