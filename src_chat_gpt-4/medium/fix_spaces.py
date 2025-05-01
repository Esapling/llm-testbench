"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def fix_spaces(text):
    """ Replace spaces with underscores and consecutive spaces with hyphens """
    text = text.replace('  ', ' -')
    return text.replace(' ', '_')

class Test(unittest.TestCase):
    def test_fix_spaces(self):
        self.assertEqual(fix_spaces('Example'), 'Example')
        self.assertEqual(fix_spaces('Example 1'), 'Example_1')
        self.assertEqual(fix_spaces(' Example 2'), '_Example_2')
        self.assertEqual(fix_spaces(' Example   3'), '_Example-3')

if __name__ == "__main__":
    unittest.main()
