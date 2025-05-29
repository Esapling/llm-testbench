"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
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
    
    # Find the longest palindromic suffix
    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            # Found the longest palindromic suffix
            # Append the reverse of the remaining prefix
            return string + string[i:][::-1]
    
    # If no palindromic suffix found (should not happen as the empty string is a palindrome)
    return string + string[:-1][::-1]


import unittest

class TestMakePalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(make_palindrome(''), '')
    
    def test_single_char(self):
        self.assertEqual(make_palindrome('a'), 'a')
    
    def test_already_palindrome(self):
        self.assertEqual(make_palindrome('racecar'), 'racecar')
        self.assertEqual(make_palindrome('level'), 'level')
    
    def test_example_cases(self):
        self.assertEqual(make_palindrome('cat'), 'catac')
        self.assertEqual(make_palindrome('cata'), 'catac')
    
    def test_palindromic_prefix(self):
        self.assertEqual(make_palindrome('abc'), 'abcba')
        self.assertEqual(make_palindrome('radar gun'), 'radar gunug radar')
    
    def test_partial_palindrome(self):
        self.assertEqual(make_palindrome('abac'), 'abacaba')
        self.assertEqual(make_palindrome('abba cat'), 'abba catac abba')
    #### PHASE 2 Tests ####
    
    def test_two_characters(self):
        self.assertEqual(make_palindrome('ab'), 'aba')
        self.assertEqual(make_palindrome('aa'), 'aa')
        self.assertEqual(make_palindrome('zy'), 'zyz')

    def test_strings_with_palindromic_suffixes(self):
        self.assertEqual(make_palindrome('madama'), 'madamadam')
        self.assertEqual(make_palindrome('rotavatorot'), 'rotavatorotavator')

    def test_strings_with_special_characters(self):
        self.assertEqual(make_palindrome('a!b!c'), 'a!b!c!b!a')
        self.assertEqual(make_palindrome('race@car'), 'race@carac@ecar')

    def test_case_sensitivity(self):
        self.assertEqual(make_palindrome('Racecar'), 'RacecaracecaR')
        self.assertEqual(make_palindrome('Level'), 'LeveleveL')

    def test_long_strings(self):
        self.assertEqual(make_palindrome('abcdefgh'), 'abcdefghgfedcba')
        self.assertEqual(make_palindrome('a' * 1000), 'a' * 1000)
        long_palindrome ="saippuakivikauppias"
        self.assertEqual(make_palindrome(long_palindrome[:-3]), long_palindrome)

if __name__ == "__main__":
    unittest.main()
