"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest
from typing import List

def select_words(s: str, n: int) -> List[str]:
    """Given a string s and a natural number n, you have been tasked to implement
    a function that returns a list of all words from string s that contain exactly
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words(""Mary had a little lamb"", 4) ==> [""little""]
    select_words(""Mary had a little lamb"", 3) ==> [""Mary"", ""lamb""]
    select_words(""simple white space"", 2) ==> []
    select_words(""Hello world"", 4) ==> [""world""]
    select_words(""Uncle sam"", 3) ==> [""Uncle""]
    """
    if not s:
        return []

    vowels = set("aeiouAEIOU")
    words = s.split()
    result_words = []

    for word in words:
        consonant_count = 0
        for char in word:
            if char.isalpha() and char not in vowels:
                consonant_count += 1
        if consonant_count == n:
            result_words.append(word)

    return result_words

class TestSelectWords(unittest.TestCase):

    def test_example_1(self):
        """Test the first example case."""
        self.assertEqual(select_words("Mary had a little lamb", 4), ["little"])

    def test_example_2(self):
        """Test the second example case."""
        self.assertEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])

    def test_empty_string(self):
        """Test with an empty input string."""
        self.assertEqual(select_words("", 5), [])

    def test_n_is_zero(self):
        """Test when the required number of consonants is zero."""
        self.assertEqual(select_words("a e i o u", 0), ["a", "e", "i", "o", "u"])
        self.assertEqual(select_words("apple banana", 0), []) # No words with 0 consonants here

    def test_mixed_case_and_consonant_count(self):
        """Test with mixed-case words and a specific consonant count."""
        self.assertEqual(select_words("Hello World", 4), ["World"])
        self.assertEqual(select_words("PYTHON is Fun", 4), ["PYTHON"])

    #------------ Phase 2 Tests ------------

    def test_case_sensitivity(self):
        self.assertEqual(select_words("Hello Programming world with Python", 3), ["Hello", "with"])
    
    def test_n_is_greater_than_word_length(self):
        self.assertEqual(select_words("abc", 5), [])
        self.assertEqual(select_words("Hello Programming world with Python", 30), [])
    def test_n_is_negative(self):
        self.assertEqual(select_words("Hello world", -1), [])
        self.assertEqual(select_words("Software quality lecture is great", -2), [])

    def test_inputs_with_no_matching_consonants(self):
        self.assertEqual(select_words("Software Quality is important", 2), [])

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

# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)