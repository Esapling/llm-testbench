"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, ""2,3"") ➞ ""2,3""
    compare_one(""5,1"", ""6"") ➞ ""6""
    compare_one(""1"", 1) ➞ None
    """
    def _to_float(value):
        if isinstance(value, (int, float)):
            return float(value)
        elif isinstance(value, str):
            # Handle both '.' and ',' as decimal separators
            return float(value.replace(',', '.'))
        else:
            # This case should ideally not happen based on the problem description
            # but added for robustness. Raising an error might also be an option.
            return float('-inf') # Treat unknown types as very small for comparison

    float_a = _to_float(a)
    float_b = _to_float(b)

    if float_a > float_b:
        return a
    elif float_b > float_a:
        return b
    else:
        # Values are equal
        return None

class TestCompareOne(unittest.TestCase):

    def test_example_1_int_vs_float(self):
        """Test the first example case: integer vs float."""
        self.assertEqual(compare_one(1, 2.5), 2.5)

    def test_example_2_int_vs_string_comma(self):
        """Test the second example case: integer vs string with comma."""
        self.assertEqual(compare_one(1, "2,3"), "2,3")

    def test_example_3_string_comma_vs_string_dot(self):
        """Test the third example case: string with comma vs string with dot."""
        self.assertEqual(compare_one("5,1", "6"), "6") # "6" is treated as 6.0

    def test_example_4_equal_values_different_types(self):
        """Test the fourth example case: equal values of different types."""
        self.assertEqual(compare_one("1", 1), None)

    def test_negative_floats(self):
        """Test with negative floating-point numbers (including as strings)."""
        self.assertEqual(compare_one(-1.5, -1.6), -1.5)
        self.assertEqual(compare_one("-2.5", "-2.6"), "-2.5")
        self.assertEqual(compare_one("-1,0", -1.0), None)


# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)