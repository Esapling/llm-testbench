def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if is_palindrome(string):
        return string
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]
    return ""

import unittest

class TestMakePalindrome(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(make_palindrome(''), '')
    def test_cat(self):
        self.assertEqual(make_palindrome('cat'), 'catac')
    def test_cata(self):
        self.assertEqual(make_palindrome('cata'), 'catac')
    def test_aba(self):
        self.assertEqual(make_palindrome('aba'), 'aba')