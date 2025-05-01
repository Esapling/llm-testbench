"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
from typing import List
import unittest

def select_words(s: str, n: int) -> List[str]:
    """Given a string s and a natural number n, return a list of all words from s
    that contain exactly n consonants, in order these words appear in the string s.
    """
    if not s:
        return []
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    result = []
    for word in s.split():
        consonant_count = sum(1 for char in word if char.isalpha() and char not in vowels)
        if consonant_count == n:
            result.append(word)
    return result

class TestSelectWords(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(select_words("Mary had a little lamb", 4), ["little"])
    
    def test_example2(self):
        self.assertEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])
    
    def test_no_matches(self):
        self.assertEqual(select_words("simple white space", 2), [])
    
    def test_case_sensitivity(self):
        self.assertEqual(select_words("Hello world", 4), ["world"])
    
    def test_mixed_case(self):
        self.assertEqual(select_words("Uncle sam", 3), ["Uncle"])

if __name__ == "__main__":
    unittest.main()