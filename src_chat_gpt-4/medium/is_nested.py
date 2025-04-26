import unittest

def is_nested(string):
    """ Check if there is a valid nested sequence of brackets """
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if not stack:
                return False
            stack.pop()
    return len(stack) > 0

class Test(unittest.TestCase):
    def test_is_nested(self):
        self.assertTrue(is_nested('[[]]'))
        self.assertFalse(is_nested('[]]]]]]][[[[[]'))
        self.assertFalse(is_nested('[][]'))
        self.assertFalse(is_nested('[]'))
        self.assertTrue(is_nested('[[][]]'))
        self.assertTrue(is_nested('[[]][['))

if __name__ == "__main__":
    unittest.main()
