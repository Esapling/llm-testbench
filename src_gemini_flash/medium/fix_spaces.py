"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores,
    and if a string has more than 2 consecutive spaces,
    then replace all consecutive spaces with -

    fix_spaces(""Example"") == ""Example""
    fix_spaces(""Example 1"") == ""Example_1""
    fix_spaces("" Example 2"") == ""_Example_2""
    fix_spaces("" Example   3"") == ""_Example-3""
    """
    result = ""
    space_count = 0

    for char in text:
        if char == ' ':
            space_count += 1
        else:
            if space_count == 1:
                result += "_"
            elif space_count == 2:
                result += "__"
            elif space_count > 2:
                result += "-"
            result += char
            space_count = 0

    # Handle any trailing spaces
    if space_count == 1:
        result += "_"
    elif space_count == 2:
        result += "__"
    elif space_count > 2:
        result += "-"

    return result

class TestFixSpaces(unittest.TestCase):

    def test_no_and_single_spaces(self):
        """Test cases with no spaces and single spaces."""
        self.assertEqual(fix_spaces("Example"), "Example")
        self.assertEqual(fix_spaces("Example 1"), "Example_1")
        self.assertEqual(fix_spaces("a b c"), "a_b_c")

    def test_examples_with_leading_and_multiple_spaces(self):
        """Test examples with leading spaces and more than two consecutive spaces."""
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")
        self.assertEqual(fix_spaces(" Example   3"), "_Example-3")

    def test_empty_string(self):
        """Test with an empty input string."""
        self.assertEqual(fix_spaces(""), "")

    def test_exactly_two_consecutive_spaces(self):
        """Test with exactly two consecutive spaces."""
        self.assertEqual(fix_spaces("a  b"), "a__b")
        self.assertEqual(fix_spaces("  leading two"), "__leading_two")
        self.assertEqual(fix_spaces("trailing two  "), "trailing_two__")

    def test_more_than_two_consecutive_spaces(self):
        """Test with more than two consecutive spaces (3 or more)."""
        self.assertEqual(fix_spaces("a   b"), "a-b")
        self.assertEqual(fix_spaces("a    b"), "a-b")
        self.assertEqual(fix_spaces("   leading three"), "-leading_three")
        self.assertEqual(fix_spaces("trailing three   "), "trailing_three-")
        self.assertEqual(fix_spaces("a     b"), "a-b") # 5 spaces

# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)