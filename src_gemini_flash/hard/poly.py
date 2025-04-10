import unittest
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

    # Simple linear equation
    if len(xs) == 2:
        a, b = xs
        return -a / b

    # Quadratic equation (more robust)
    if len(xs) == 3:
        a, b, c = xs
        delta = b**2 - 4 * a * c
        if delta >= 0:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            # Return the real root closest to zero
            if abs(x1) <= abs(x2):
                return x1
            else:
                return x2
        else:
            # Handle complex roots if needed, for simplicity return None here
            return None

    # For higher order polynomials, numerical methods are needed
    # A simple bisection method is used here for demonstration
    a = -10.0
    b = 10.0
    for _ in range(100):  # Iterate a fixed number of times
        mid = (a + b) / 2
        if abs(poly(xs, mid)) < 1e-6:  # Check for approximate zero
            return mid
        if poly(xs, a) * poly(xs, mid) < 0:
            b = mid
        else:
            a = mid
    return mid  # Return the approximate zero found


class TestFindZero(unittest.TestCase):
    def test_find_zero(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=5)
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=5)
        self.assertAlmostEqual(find_zero([0, 5]), 0.0, places=5)
        self.assertAlmostEqual(find_zero([1, -5, 6]), 2.0, places=5)  # Roots are 2 and 3, returns closest to 0
        self.assertAlmostEqual(find_zero([-2, 0, 1]), -1.4142135623730951, places=5)  # Roots are sqrt(2) and -sqrt(2)
        self.assertAlmostEqual(find_zero([1, -1]), 1.0, places=5)


if __name__ == '__main__':
    unittest.main()