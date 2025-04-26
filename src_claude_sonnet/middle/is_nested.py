def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    # First, check for valid nesting
    stack = []
    valid_pairs = []
    
    for i, char in enumerate(string):
        if char == '[':
            stack.append(i)
        elif char == ']' and stack:
            open_index = stack.pop()
            valid_pairs.append((open_index, i))
    
    # Check if there's any nested bracket
    for i, j in valid_pairs:
        for m, n in valid_pairs:
            if i < m and n < j:  # This means bracket (m,n) is inside bracket (i,j)
                return True
    
    return False

import unittest

class TestIsNested(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(is_nested('[[]]'))
        self.assertFalse(is_nested('[]]]]]]][[[[[]'))
        self.assertFalse(is_nested('[][]'))
        self.assertFalse(is_nested('[]'))
        self.assertTrue(is_nested('[[][]]'))
        self.assertTrue(is_nested('[[]][['))
        
    def test_simple_nested(self):
        self.assertTrue(is_nested('[[[]]]]'))
        
    def test_not_nested(self):
        self.assertFalse(is_nested('[][][][][]'))
        
    def test_complex_cases(self):
        self.assertTrue(is_nested('[[]][][][[]]'))
        self.assertTrue(is_nested('[[][[]]]'))
        
    def test_unbalanced_brackets(self):
        self.assertFalse(is_nested('['))
        self.assertTrue(is_nested('[[[]]'))
        
    def test_empty_string(self):
        self.assertFalse(is_nested(''))

if __name__ == "__main__":
    unittest.main()
