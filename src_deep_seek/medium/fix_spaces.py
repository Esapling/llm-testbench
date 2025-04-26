import unittest
import re

def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    """
    # Replace more than 2 consecutive spaces with -
    text = re.sub(r' {3,}', '-', text)
    # Replace remaining single spaces with _
    text = re.sub(r' ', '_', text)
    return text

class TestFixSpaces(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(fix_spaces("Example"), "Example")
    
    def test_example2(self):
        self.assertEqual(fix_spaces("Example 1"), "Example_1")
    
    def test_example3(self):
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")
    
    def test_example4(self):
        self.assertEqual(fix_spaces(" Example   3"), "_Example-3")
    
    def test_multiple_spaces(self):
        self.assertEqual(fix_spaces("a  b   c    d"), "a_b-c-d")
    
    def test_only_spaces(self):
        self.assertEqual(fix_spaces("   "), "-")

if __name__ == "__main__":
    unittest.main()