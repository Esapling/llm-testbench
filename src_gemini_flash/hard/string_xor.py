"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if len(a) != len(b):
        # Although the docstring implies inputs of the same length,
        # a robust implementation might handle this, but based on the prompt
        # we assume equal length. If they were of different lengths,
        # padding or raising an error would be options.
        # For this problem, we assume equal length based on the typical use case
        # and the single example provided.
        pass # Or raise an error if necessary

    result = []
    for i in range(len(a)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return "".join(result)

class TestStringXOR(unittest.TestCase):

    def test_example_case(self):
        """Test the example case from the docstring."""
        self.assertEqual(string_xor('010', '110'), '100')

    def test_equal_strings_all_zeros(self):
        """Test XOR of two strings of all zeros."""
        self.assertEqual(string_xor('0000', '0000'), '0000')

    def test_equal_strings_all_ones(self):
        """Test XOR of two strings of all ones."""
        self.assertEqual(string_xor('111', '111'), '000')

    def test_mixed_strings(self):
        """Test XOR of mixed zero and one strings."""
        self.assertEqual(string_xor('10101', '01010'), '11111')
        self.assertEqual(string_xor('110011', '101010'), '011001')

    def test_single_character_strings(self):
        """Test with single character strings."""
        self.assertEqual(string_xor('0', '1'), '1')
        self.assertEqual(string_xor('1', '0'), '1')
        self.assertEqual(string_xor('0', '0'), '0')
        self.assertEqual(string_xor('1', '1'), '0')

    # ----------- Phase 2 Tests -----------
    
    def test_empty_strings(self):
        self.assertEqual(string_xor('', ''), '')
        self.assertEqual(string_xor('1010', ''), '1010')
        self.assertEqual(string_xor('', '1100'), '1100')

    def test_long_strings(self):
        self.assertEqual(string_xor('11001100', '10101010'), '01100110')
        self.assertEqual(string_xor('11110000', '00001111'), '11111111')
        self.assertEqual(string_xor('00000000', '11111111'), '11111111')
        self.assertEqual(string_xor('10101010', '10101010'), '00000000')
    
    def test_different_length_strings(self):
        self.assertEqual(string_xor('1', '0101'), '1100')
        self.assertEqual(string_xor('111', '1'), '110')
        self.assertEqual(string_xor('', '1010'), '1010')

    def test_all_same(self):
        self.assertEqual(string_xor('00000000', '00000000'), '00000000')
        self.assertEqual(string_xor('11111111', '11111111'), '00000000')
        
    def test_all_different(self):
        self.assertEqual(string_xor('01010101', '10101010'), '11111111')
        self.assertEqual(string_xor('11001100', '00110011'), '11111111')
    
    

# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)