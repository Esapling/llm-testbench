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

    #------------ Phase 2 Tests ------------
    def test_empty_string(self):
        self.assertEqual(select_words("", 0), [])
        self.assertEqual(select_words("", 100), [])
   
    def test_n_is_greater_than_word_length(self):
        self.assertEqual(select_words("abc", 5), [])
        self.assertEqual(select_words("Hello Programming world with Python", 30), [])
    def test_n_is_negative(self):
        self.assertEqual(select_words("Hello world", -1), [])
        self.assertEqual(select_words("Software quality lecture is great", -2), [])

    def test_zero_consonants(self):
        self.assertEqual(select_words("a e i", 0), ["a", "e", "i"])
    
    def test_inputs_with_all_matching_consonants(self):
        self.assertEqual(select_words("abcd xayz tlmu", 3), ["abcd", "xayz", "tlmu"])

    def test_inputs_with_no_consonants(self):
        self.assertEqual(select_words("aeiou", 0), ["aeiou"])
        self.assertEqual(select_words("AEIOU", 0), ["AEIOU"])    

    def test_extremely_long_string(self):
        long_string = "a" * 100 + "b" * 100 + "c" * 100
        self.assertEqual(select_words(long_string, 200), ["a" * 100 + "b" * 100 + "c" * 100])
        # self.assertEqual(select_words(long_string, 2000), [])
        # self.assertEqual(select_words(long_string, 1500), ["a" * 1000 + "b" * 1000])
if __name__ == "__main__":
    unittest.main()