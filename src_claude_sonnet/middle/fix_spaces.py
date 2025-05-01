"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    result = ""
    i = 0
    
    while i < len(text):
        if text[i] == " ":
            # Count consecutive spaces
            space_count = 0
            while i < len(text) and text[i] == " ":
                space_count += 1
                i += 1
                
            # Replace spaces based on count
            if space_count > 2:
                result += "-"
            else:
                result += "_" * space_count
        else:
            result += text[i]
            i += 1
    
    return result

import unittest

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
        self.assertEqual(fix_spaces(" Hello  World   !"), "_Hello-World-!")

if __name__ == "__main__":
    unittest.main()
