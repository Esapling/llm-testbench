"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def is_equal_to_sum_even(n: int) -> bool:
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # A sum of 4 positive even numbers (2k1 + 2k2 + 2k3 + 2k4 where ki >= 1)
    # is equal to 2 * (k1 + k2 + k3 + k4).
    # The minimum value of k1 + k2 + k3 + k4 is 1 + 1 + 1 + 1 = 4.
    # So the minimum sum is 2 * 4 = 8.
    # The sum must also be an even number.
    return n >= 8 and n % 2 == 0

class TestIsEqualToSumEven(unittest.TestCase):

    def test_examples_less_than_8(self):
        """Test the example cases less than 8."""
        self.assertEqual(is_equal_to_sum_even(4), False)
        self.assertEqual(is_equal_to_sum_even(6), False)

    def test_example_equal_to_8(self):
        """Test the example case equal to 8."""
        self.assertEqual(is_equal_to_sum_even(8), True)

    def test_even_greater_than_8(self):
        """Test an even number greater than 8."""
        self.assertEqual(is_equal_to_sum_even(10), True)
        self.assertEqual(is_equal_to_sum_even(12), True)

    def test_odd_number(self):
        """Test odd numbers."""
        self.assertEqual(is_equal_to_sum_even(7), False)
        self.assertEqual(is_equal_to_sum_even(9), False)
        self.assertEqual(is_equal_to_sum_even(11), False)

    def test_numbers_less_than_8_and_odd(self):
        """Test odd numbers less than 8."""
        self.assertEqual(is_equal_to_sum_even(1), False)
        self.assertEqual(is_equal_to_sum_even(3), False)
        self.assertEqual(is_equal_to_sum_even(5), False)

# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)