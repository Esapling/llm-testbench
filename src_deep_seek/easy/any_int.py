"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    if not all(isinstance(num, int) for num in [x, y, z]):
        return False
    return (x == y + z) or (y == x + z) or (z == x + y)

class TestAnyInt(unittest.TestCase):
    def test_true_case1(self):
        self.assertTrue(any_int(5, 2, 7))
    
    def test_false_case(self):
        self.assertFalse(any_int(3, 2, 2))
    
    def test_true_with_negative(self):
        self.assertTrue(any_int(3, -2, 1))
    
    def test_non_integers(self):
        self.assertFalse(any_int(3.6, -2.2, 2))
    
    def test_all_zero(self):
        self.assertTrue(any_int(0, 0, 0))

if __name__ == "__main__":
    unittest.main()