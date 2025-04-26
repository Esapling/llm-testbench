import unittest

def derivative(xs: list):
    """ Return derivative of polynomial represented by coefficients xs """
    return [i * coeff for i, coeff in enumerate(xs)][1:]

class TestDerivative(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])
    
    def test_example2(self):
        self.assertEqual(derivative([1, 2, 3]), [2, 6])
    
    def test_constant(self):
        self.assertEqual(derivative([5]), [])
    
    def test_empty(self):
        self.assertEqual(derivative([]), [])

if __name__ == "__main__":
    unittest.main()