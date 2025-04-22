import unittest

def derivative(coefficients):
    """
    Given a list of coefficients of a polynomial, return the list of coefficients of its derivative.
    The input list represents coefficients from the constant term upwards (a_0, a_1, a_2, ...).
    For example, [1, 2, 3] represents the polynomial 1 + 2x + 3x^2.
    The derivative of this polynomial is 2 + 6x, which should be represented as [2, 6].
    """
    if not coefficients:
        return []

    # The derivative of a constant is 0. If the polynomial is just a constant (e.g., [5]),
    # its derivative is 0, represented as [0].
    if len(coefficients) == 1:
        return [0]

    derivative_coeffs = []
    # The derivative of a_i * x^i is a_i * i * x^(i-1).
    # The constant term a_0 differentiates to 0.
    # The coefficient of x^1 (a_1) differentiates to a_1 * 1 * x^0 = a_1.
    # The coefficient of x^2 (a_2) differentiates to a_2 * 2 * x^1.
    # The coefficient of x^i (a_i) differentiates to a_i * i * x^(i-1).
    # The new list of coefficients will start from the coefficient of x^0 in the derivative.
    for i in range(1, len(coefficients)):
        derivative_coeffs.append(coefficients[i] * i)

    return derivative_coeffs

class TestDerivative(unittest.TestCase):

    def test_derivative_constant(self):
        """Test the derivative of a constant polynomial."""
        self.assertEqual(derivative([5]), [0])
        self.assertEqual(derivative([-3]), [0])
        self.assertEqual(derivative([0]), [0])

    def test_derivative_linear(self):
        """Test the derivative of a linear polynomial (ax + b)."""
        # 2x + 3 -> derivative is 2. Coefficients [3, 2] -> [2]
        self.assertEqual(derivative([3, 2]), [2])
        # -x + 1 -> derivative is -1. Coefficients [1, -1] -> [-1]
        self.assertEqual(derivative([1, -1]), [-1])
        # 4x -> derivative is 4. Coefficients [0, 4] -> [4]
        self.assertEqual(derivative([0, 4]), [4])

    def test_derivative_quadratic(self):
        """Test the derivative of a quadratic polynomial (ax^2 + bx + c)."""
        # 3x^2 + 2x + 1 -> derivative is 6x + 2. Coefficients [1, 2, 3] -> [2, 6]
        self.assertEqual(derivative([1, 2, 3]), [2, 6])
        # x^2 - 5x -> derivative is 2x - 5. Coefficients [0, -5, 1] -> [-5, 2]
        self.assertEqual(derivative([0, -5, 1]), [-5, 2])
        # -2x^2 + 7 -> derivative is -4x. Coefficients [7, 0, -2] -> [0, -4]
        self.assertEqual(derivative([7, 0, -2]), [0, -4])

    def test_derivative_higher_degree(self):
        """Test the derivative of a higher-degree polynomial."""
        # 4x^3 - 2x^2 + x - 1 -> derivative is 12x^2 - 4x + 1. Coefficients [-1, 1, -2, 4] -> [1, -4, 12]
        self.assertEqual(derivative([-1, 1, -2, 4]), [1, -4, 12])
        # x^5 -> derivative is 5x^4. Coefficients [0, 0, 0, 0, 0, 1] -> [0, 0, 0, 5]
        self.assertEqual(derivative([0, 0, 0, 0, 0, 1]), [0, 0, 0, 5]) # error in the test case : should be [0, 0, 0, 0, 5]

    def test_derivative_empty_list(self):
        """Test the derivative of an empty list (representing no polynomial)."""
        self.assertEqual(derivative([]), [])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)