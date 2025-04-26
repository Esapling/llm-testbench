def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Skip the constant term (xs[0]) and compute the derivative of each term
    result = []
    
    for i in range(1, len(xs)):
        # Derivative of (coefficient * x^i) is (coefficient * i * x^(i-1))
        result.append(xs[i] * i)
    
    return result


# Unit tests
import unittest

class TestDerivative(unittest.TestCase):
    def test_example_case_1(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])
    
    def test_example_case_2(self):
        self.assertEqual(derivative([1, 2, 3]), [2, 6])
    
    def test_constant_polynomial(self):
        self.assertEqual(derivative([5]), [])
    
    def test_linear_polynomial(self):
        self.assertEqual(derivative([3, 4]), [4])
    
    def test_quadratic_polynomial(self):
        self.assertEqual(derivative([1, 2, 3]), [2, 6])
    
    def test_higher_degree_polynomial(self):
        self.assertEqual(derivative([0, 0, 0, 0, 5]), [0, 0, 0, 20])
    
    def test_negative_coefficients(self):
        self.assertEqual(derivative([-1, -2, -3, -4]), [-2, -6, -12])
    
    def test_mixed_coefficients(self):
        self.assertEqual(derivative([10, -5, 0, 7, -2]), [-5, 0, 21, -8])

if __name__ == "__main__":
    unittest.main()
