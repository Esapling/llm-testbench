import unittest

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
    # Check if all inputs are pure integers (not booleans)
    for val in [x, y, z]:
        if isinstance(val, bool) or not isinstance(val, int):
            return False
    
    # Check if any number equals the sum of the other two
    return (x == y + z) or (y == x + z) or (z == x + y)


class TestAnyInt(unittest.TestCase):
    
    def test_valid_sum_cases(self):
        """Test cases where one number equals the sum of the other two"""
        self.assertTrue(any_int(5, 2, 7))  # 7 = 5 + 2
        self.assertTrue(any_int(3, -2, 1))  # 1 = 3 + (-2)
        self.assertTrue(any_int(0, 5, -5))  # 0 = 5 + (-5)
        self.assertTrue(any_int(10, -3, 7))  # 10 = (-3) + 7
    
    def test_invalid_sum_cases(self):
        """Test cases where no number equals the sum of the other two"""
        self.assertFalse(any_int(3, 2, 2))  # No valid sum
        self.assertFalse(any_int(1, 2, 4))  # No valid sum
        self.assertFalse(any_int(5, 5, 5))  # No valid sum
    
    def test_float_inputs(self):
        """Test that float inputs return False"""
        self.assertFalse(any_int(3.6, -2.2, 2))  # Contains floats
        self.assertFalse(any_int(5.0, 2, 7))  # 5.0 is float even if whole number
        self.assertFalse(any_int(1, 2.5, 3))  # Contains float
    
    def test_boolean_inputs(self):
        """Test that boolean inputs return False (explicitly excluded)"""
        self.assertFalse(any_int(True, 1, 2))  # Boolean input
        self.assertFalse(any_int(1, False, 1))  # Boolean input
        self.assertFalse(any_int(True, False, 1))  # Multiple booleans
    
    
    def test_mixed_invalid_types(self):
        """Test various invalid input types"""
        self.assertFalse(any_int("1", 2, 3))  # String input
        self.assertFalse(any_int(1, None, 3))  # None input
        self.assertFalse(any_int(1, 2, [3]))  # List input

    def test_examples(self):
        self.assertTrue(any_int(5, 2, 7))
        self.assertFalse(any_int(3, 2, 2))
        self.assertTrue(any_int(3, -2, 1))
        self.assertFalse(any_int(3.6, -2.2, 2))
    
        #------------ Phase 2 Tests ------------
    
    def test_string_inputs(self):
        self.assertFalse(any_int("5", 2, 7))
    
    def test_large_numbers(self):
        self.assertTrue(any_int(1000000, 2000000, 3000000))
        self.assertFalse(any_int(1000000, 2000000, 4000000))
        self.assertTrue(any_int(-1000000, -2000000, -3000000))
        self.assertFalse(any_int(-1000000, -2000000, -4000000))

    def test_all_zero(self):
        self.assertTrue(any_int(0, 0, 0))

if __name__ == '__main__':
    unittest.main()