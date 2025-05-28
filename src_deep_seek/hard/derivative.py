"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
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

    # -------------- Phase 2 Tests -------------
    
    def test_zero_polynomial(self):
        self.assertEqual(derivative([0, 0, 0]), [0, 0])
    
    def test_high_degree(self):
        self.assertEqual(derivative([2, 3, 4, 5, 7, 15, 6]), [3, 8, 15, 28, 75, 36])
        
    def test_negative_coefficients(self):
        self.assertEqual(derivative([-1, -2, -3]), [-2, -6])
        self.assertEqual(derivative([-5, 0, 3]), [0, 6])
    
    def test_large_coefficients(self):
        self.assertEqual(derivative([1000, 2000, 3000]), [2000, 6000])
        self.assertEqual(derivative([1000000, 500000, 250000]), [500000, 500000])

if __name__ == "__main__":
    unittest.main()