"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def is_palindrome(string: str) -> bool:
    """Test if given string is a palindrome"""
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string."""
    if not string:
        return ''
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]
    return string

class Test(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(make_palindrome(''), '')
    def test_cat(self):
        self.assertEqual(make_palindrome('cat'), 'catac')
    def test_cata(self):
        self.assertEqual(make_palindrome('cata'), 'catac')
    def test_palindrome(self):
        self.assertEqual(make_palindrome('racecar'), 'racecar')

if __name__ == "__main__":
    unittest.main()
