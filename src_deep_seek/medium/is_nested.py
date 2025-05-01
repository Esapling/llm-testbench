"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.
    '''
    stack = []
    has_nested = False
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if len(stack) > 1:
                has_nested = True
            if stack:
                stack.pop()
    return has_nested

class TestIsNested(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(is_nested('[[]]'))
    
    def test_example2(self):
        self.assertFalse(is_nested('[]]]]]]][[[[[]'))
    
    def test_example3(self):
        self.assertFalse(is_nested('[][]'))
    
    def test_example4(self):
        self.assertFalse(is_nested('[]'))
    
    def test_example5(self):
        self.assertTrue(is_nested('[[][]]'))
    
    def test_example6(self):
        self.assertTrue(is_nested('[[]][['))

if __name__ == "__main__":
    unittest.main()