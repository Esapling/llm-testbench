import re
import unittest
import re

def fix_spaces(text):
    # First, replace all groups of 3 or more spaces with a dash
    text = re.sub(r' {3,}', '-', text)
    # Then, replace every single space with an underscore
    text = text.replace(' ', '_')
    return text

class TestFixSpaces(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(fix_spaces("Example"), "Example")
        self.assertEqual(fix_spaces("Example 1"), "Example_1")
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")
        self.assertEqual(fix_spaces(" Example   3"), "_Example-3")
        
    def test_no_spaces(self):
        self.assertEqual(fix_spaces("HelloWorld"), "HelloWorld")
        
    def test_single_spaces(self):
        self.assertEqual(fix_spaces("Hello World"), "Hello_World")
        
    def test_multiple_spaces(self):
        self.assertEqual(fix_spaces("Hello   World"), "Hello-World")
        self.assertEqual(fix_spaces("Hello    World"), "Hello-World")
        
    def test_leading_spaces(self):
        self.assertEqual(fix_spaces("   Hello"), "-Hello")
        
    def test_trailing_spaces(self):
        self.assertEqual(fix_spaces("Hello   "), "Hello-")
        
    def test_mixed_spaces(self):
        self.assertEqual(fix_spaces(" Hello  World   !"), "_Hello__World-!")

    # --------------- Phase 2 Tests --------------

    def test_only_spaces(self):
        self.assertEqual(fix_spaces('   '), '-')
        self.assertEqual(fix_spaces('      '), '-')
        self.assertEqual(fix_spaces(' '), '_')
    
    def test_empty_string(self):
        self.assertEqual(fix_spaces(''), '')
    

if __name__ == "__main__":
    unittest.main()
