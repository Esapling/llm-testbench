import unittest


def derivative(coefficients):
    """
    Given a list of coefficients of a polynomial, return the list of coefficients of its derivative.
    """
    if not coefficients:
        return []

    if len(coefficients) == 1:
        return [0]

    derivative_coeffs = []
    for i in range(1, len(coefficients)):
        derivative_coeffs.append(coefficients[i] * i)

    return derivative_coeffs


class TestDerivative(unittest.TestCase):
    def test_derivative(self):
        self.assertEqual(derivative([1, 2, 1]), [2, 2])
        self.assertEqual(derivative([0, 1, 2, 3]), [1, 4, 9])
        self.assertEqual(derivative([5]), [0])
        self.assertEqual(derivative([]), [])
        self.assertEqual(derivative([0, 0, 0, 0]), [0, 0, 0])
        self.assertEqual(derivative([-1, 2, -3, 4]), [2, -6, 12])


if __name__ == '__main__':
    unittest.main()