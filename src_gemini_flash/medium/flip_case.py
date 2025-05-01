"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Using the built-in swapcase() method as it directly addresses the requirement
    return string.swapcase()

class TestFlipCase(unittest.TestCase):

    def test_example_case(self):
        """Test the example case from the docstring."""
        self.assertEqual(flip_case('Hello'), 'hELLO')

    def test_all_lowercase(self):
        """Test with an all-lowercase string."""
        self.assertEqual(flip_case('world'), 'WORLD')

    def test_all_uppercase(self):
        """Test with an all-uppercase string."""
        self.assertEqual(flip_case('PYTHON'), 'python')

    def test_mixed_case_with_non_letters(self):
        """Test with a string containing mixed-case letters and other characters."""
        self.assertEqual(flip_case('MiXeD cAsE 123 !'), 'mIXeD CaSe 123 !')

    def test_empty_string(self):
        """Test with an empty input string."""
        self.assertEqual(flip_case(''), '')

# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)