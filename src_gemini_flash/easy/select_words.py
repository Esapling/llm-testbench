import unittest


def select_words(st):
    """
    Given a string, return a new string with the words that start with 'a'
    or with 'b'.
    Words are separated by a space. Don't treat numbers as a special case.
    select_words("apple banana cherry avocado aardvark") == "apple banana avocado aardvark"
    select_words("dog cat mouse ball") == "ball"
    select_words("ant zebra bee") == "ant bee"
    """
    words = st.split()
    selected_words = [word for word in words if word[0] in 'ab']
    return " ".join(selected_words)


class TestSelectWords(unittest.TestCase):
    def test_select_words(self):
        self.assertEqual(select_words("apple banana cherry avocado aardvark"), "apple banana avocado aardvark")
        self.assertEqual(select_words("dog cat mouse ball"), "ball")
        self.assertEqual(select_words("ant zebra bee"), "ant bee")
        self.assertEqual(select_words("apple Ant ball Bee"), "apple Ant ball Bee")
        self.assertEqual(select_words("123 banana apple"), "banana apple")
        self.assertEqual(select_words("cherry dog elephant frog"), "")


if __name__ == '__main__':
    unittest.main()