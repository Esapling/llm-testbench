def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    if not s:
        return []
    
    vowels = "aeiouAEIOU"
    result = []
    
    words = s.split()
    
    for word in words:
        # Count consonants in the word
        consonant_count = sum(1 for char in word if char.isalpha() and char not in vowels)
        
        # Add word to result if it has exactly n consonants
        if consonant_count == n:
            result.append(word)
    
    return result


# Unit tests
import unittest

class TestSelectWords(unittest.TestCase):
    def test_example_case_1(self):
        self.assertEqual(select_words("Mary had a little lamb", 4), ["little"])
    
    def test_example_case_2(self):
        self.assertEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])
    
    def test_example_case_3(self):
        self.assertEqual(select_words("simple white space", 2), [])
    
    def test_example_case_4(self):
        self.assertEqual(select_words("Hello world", 4), ["world"])
    
    def test_example_case_5(self):
        self.assertEqual(select_words("Uncle sam", 3), ["Uncle"])
    
    def test_empty_string(self):
        self.assertEqual(select_words("", 2), [])
    
    def test_single_word(self):
        self.assertEqual(select_words("Consonants", 6), ["Consonants"])
    
    def test_zero_consonants(self):
        self.assertEqual(select_words("a e i", 0), ["a", "e", "i"])
    
    def test_case_sensitivity(self):
        self.assertEqual(select_words("Python Java", 3), ["Python"])
    
    def test_no_matching_words(self):
        self.assertEqual(select_words("abc def ghi", 10), [])

if __name__ == "__main__":
    unittest.main()
