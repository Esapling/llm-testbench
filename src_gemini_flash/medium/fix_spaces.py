import unittest
import re


def fix_spaces(text):
    """
    Given a string, return the string with single spaces between words.
    """
    return re.sub(r'\s+', ' ', text).strip()


class TestFixSpaces(unittest.TestCase):
    def test_fix_spaces(self):
        self.assertEqual(fix_spaces("hello  world"), "hello world")
        self.assertEqual(fix_spaces("  hello world  "), "hello world")
        self.assertEqual(fix_spaces("hello   world  "), "hello world")
        self.assertEqual(fix_spaces("  hello   world"), "hello world")
        self.assertEqual(fix_spaces("hello"), "hello")
        self.assertEqual(fix_spaces("   "), "")
        self.assertEqual(fix_spaces(""), "")


if __name__ == '__main__':
    unittest.main()