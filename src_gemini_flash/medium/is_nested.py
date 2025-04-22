import unittest

def is_nested(string: str) -> bool:
    """
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    """
    open_count = 0
    for char in string:
        if char == '[':
            open_count += 1
        elif char == ']':
            if open_count > 1:
                return True
            if open_count > 0:
                open_count -= 1

    return False

class TestIsNested(unittest.TestCase):

    def test_examples_1_3_4(self):
        """Test examples [[]], [][], and []."""
        self.assertEqual(is_nested('[[]]'), True)
        self.assertEqual(is_nested('[][]'), False)
        self.assertEqual(is_nested('[]'), False)

    def test_example_2(self):
        """Test example []]]]]]][[[[[]."""
        self.assertEqual(is_nested('[]]]]]]][[[[[]'), False)

    def test_example_5(self):
        """Test example [[][]]."""
        self.assertEqual(is_nested('[[][]]'), True)

    def test_example_6(self):
        """Test example [[]][[."""
        self.assertEqual(is_nested('[[]][[ '), True) # Note: The prompt says only square brackets, but example 6 has a space. Assuming spaces should be ignored or the constraint is slightly loose in the example. Based on the implementation, non-bracket chars are ignored, which matches example 6's expected output.

    def test_edge_cases(self):
        """Test empty string and simple unbalanced strings."""
        self.assertEqual(is_nested(''), False)
        self.assertEqual(is_nested('['), False)
        self.assertEqual(is_nested(']'), False)
        self.assertEqual(is_nested('[['), False)
        self.assertEqual(is_nested(']]'), False)
        self.assertEqual(is_nested('[[['), False) # Test with more open brackets


# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)