import unittest

def any_int(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  """
    if not all(isinstance(i, int) for i in [x, y, z]):
        return False
    
    if x + y == z or x + z == y or y + z == x:
        return True
    else:
        return False

class TestAnyInt(unittest.TestCase):

    def test_example_1(self):
        """Test the first example case where one number is the sum of the others."""
        self.assertEqual(any_int(5, 2, 7), True)

    def test_example_2(self):
        """Test the second example case where all are integers but no sum matches."""
        self.assertEqual(any_int(3, 2, 2), False)

    def test_example_3_negative_numbers(self):
        """Test the third example case with negative numbers."""
        self.assertEqual(any_int(3, -2, 1), True)

    def test_example_4_non_integers(self):
        """Test the fourth example case with non-integer inputs."""
        self.assertEqual(any_int(3.6, -2.2, 2), False)

    def test_with_zeros(self):
        """Test with zero inputs."""
        self.assertEqual(any_int(0, 0, 0), True)
        self.assertEqual(any_int(1, 0, 1), True)
        self.assertEqual(any_int(1, 1, 0), True)
        self.assertEqual(any_int(0, 1, 1), True)
        self.assertEqual(any_int(0, 1, 2), False)


    def test_mixed_integer_and_non_integer(self):
        """Test cases with a mix of integer and non-integer inputs."""
        self.assertEqual(any_int(1, 2.0, 3), False)
        self.assertEqual(any_int(1.5, 2.3, 3.8), False)
        self.assertEqual(any_int(5, 2.5, 7.5), False)

# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)