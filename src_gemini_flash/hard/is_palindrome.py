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
        return ""

    for i in range(len(string), -1, -1):
        if is_palindrome(string[:i]):
            return string + string[i-1::-1]


class TestMakePalindrome(unittest.TestCase):
    def test_make_palindrome(self):
        self.assertEqual(make_palindrome(""), "")
        self.assertEqual(make_palindrome("cat"), "catac")
        self.assertEqual(make_palindrome("cata"), "catac")
        self.assertEqual(make_palindrome("racecar"), "racecar")
        self.assertEqual(make_palindrome("a"), "a")
        self.assertEqual(make_palindrome("ab"), "aba")
        self.assertEqual(make_palindrome("abc"), "abcba")


if __name__ == '__main__':
    unittest.main()