"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Ensure both strings are of equal length by padding the shorter one
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    # Perform XOR operation bit by bit
    result = ''
    for i in range(max_len):
        # XOR is 1 if bits are different, 0 if they are the same
        result += '1' if a[i] != b[i] else '0'
    
    return result


# Unit tests
import unittest

class TestStringXOR(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(string_xor('010', '110'), '100')
    
    def test_equal_length_strings(self):
        self.assertEqual(string_xor('1010', '0101'), '1111')
        self.assertEqual(string_xor('1111', '1111'), '0000')
        self.assertEqual(string_xor('0000', '0000'), '0000')
    
    def test_different_length_strings(self):
        self.assertEqual(string_xor('1', '0101'), '1100')
        self.assertEqual(string_xor('111', '1'), '110')
        self.assertEqual(string_xor('', '1010'), '1010')
    
    def test_empty_strings(self):
        self.assertEqual(string_xor('', ''), '')
    
    def test_single_bits(self):
        self.assertEqual(string_xor('0', '0'), '0')
        self.assertEqual(string_xor('1', '1'), '0')
        self.assertEqual(string_xor('0', '1'), '1')
        self.assertEqual(string_xor('1', '0'), '1')

if __name__ == "__main__":
    unittest.main()
