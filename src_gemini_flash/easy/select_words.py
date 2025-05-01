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


# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)