"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""

def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
    '''
    # Check if all numbers are integers
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        # Handle floats that are equivalent to integers
        if not (x == int(x) and y == int(y) and z == int(z)):
            return False
    
    # Check if one number equals the sum of the other two
    return x == y + z or y == x + z or z == x + y


# Unit tests
import unittest

class TestAnyInt(unittest.TestCase):
    def test_example_case_1(self):
        self.assertTrue(any_int(5, 2, 7))
    
    def test_example_case_2(self):
        self.assertFalse(any_int(3, 2, 2))
    
    def test_example_case_3(self):
        self.assertTrue(any_int(3, -2, 1))
    
    def test_example_case_4(self):
        self.assertFalse(any_int(3.6, -2.2, 2))
    
    def test_integer_floats(self):
        # Floats that are equivalent to integers should work
        self.assertTrue(any_int(5.0, 2.0, 7.0))
    
    def test_mix_integer_types(self):
        self.assertTrue(any_int(3, 2.0, 1))
    
    def test_non_integer_floats(self):
        self.assertFalse(any_int(3.5, 1.5, 2))
    
    def test_all_equal(self):
        self.assertFalse(any_int(5, 5, 5))
    
    def test_zero_values(self):
        self.assertTrue(any_int(0, 0, 0))

if __name__ == "__main__":
    unittest.main()
