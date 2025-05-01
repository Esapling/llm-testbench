"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:
        return ''

    beginning_of_suffix = 0

    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1

    return string + string[:beginning_of_suffix][::-1]

class TestMakePalindrome(unittest.TestCase):

    def test_empty_string(self):
        """Test with an empty input string."""
        self.assertEqual(make_palindrome(''), '')

    def test_example_cat(self):
        """Test with the example 'cat'."""
        self.assertEqual(make_palindrome('cat'), 'catac')

    def test_example_cata(self):
        """Test with the example 'cata'."""
        self.assertEqual(make_palindrome('cata'), 'catac')

    def test_already_palindrome(self):
        """Test with a string that is already a palindrome."""
        self.assertEqual(make_palindrome('racecar'), 'racecar')
        self.assertEqual(make_palindrome('madam'), 'madam')

    def test_complex_string(self):
        """Test with a more complex string."""
        self.assertEqual(make_palindrome('google'), 'googlelgoog')
        self.assertEqual(make_palindrome('abab'), 'ababa')

# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)