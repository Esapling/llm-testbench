"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def select_words(s, n):
    vowels = "aeiouAEIOU"
    words = s.split()
    result = []
    for word in words:
        consonants = sum(1 for c in word if c.isalpha() and c not in vowels)
        if consonants == n:
            result.append(word)
    return result

class TestSelectWords(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(select_words("Mary had a little lamb", 4), ["little"])
        self.assertEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])
        self.assertEqual(select_words("simple white space", 2), [])

if __name__ == "__main__":
    unittest.main()
