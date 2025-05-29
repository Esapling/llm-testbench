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
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return string
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]
    return string + string[:-1][::-1]

class TestMakePalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(make_palindrome(''), '')
    
    def test_example1(self):
        self.assertEqual(make_palindrome('cat'), 'catac')
    
    def test_example2(self):
        self.assertEqual(make_palindrome('cata'), 'catac')
    
    def test_already_palindrome(self):
        self.assertEqual(make_palindrome('racecar'), 'racecar')
    
    def test_single_char(self):
        self.assertEqual(make_palindrome('a'), 'a')

    #### PHASE 2 Tests ####
    def test_two_characters(self):
        self.assertEqual(make_palindrome('ab'), 'aba')
        self.assertEqual(make_palindrome('aa'), 'aa')
        self.assertEqual(make_palindrome('zy'), 'zyz')

    def test_strings_with_palindromic_suffixes(self):
        self.assertEqual(make_palindrome('madama'), 'madamadam')
        self.assertEqual(make_palindrome('rotavatorot'), 'rotavatorotavator')
    def test_strings_with_no_palindromic_suffixes(self):
        self.assertEqual(make_palindrome('hello'), 'hellolleh')
        self.assertEqual(make_palindrome('world'), 'worldlrow')

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