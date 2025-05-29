from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    string_xor('010', '110')
    '100'
    """
    max_len = max(len(a), len(b))
    
    # Pad the shorter string with '0's on the right
    a = a.ljust(max_len, '0')
    b = b.ljust(max_len, '0')
    
    result = []
    for i in range(max_len):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
            
    return "".join(result)


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
        self.assertEqual(string_xor('1', '0101'), '1101') # 1000 0101 -> 1101 | 0001 0101 -> 0100
        self.assertEqual(string_xor('111', '100'), '011')
        self.assertEqual(string_xor('', '1010'), '1010')
    
    def test_empty_strings(self):
        self.assertEqual(string_xor('', ''), '')
    
    def test_single_bits(self):
        self.assertEqual(string_xor('0', '0'), '0')
        self.assertEqual(string_xor('1', '1'), '0')
        self.assertEqual(string_xor('0', '1'), '1')
        self.assertEqual(string_xor('1', '0'), '1')
        
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

if __name__ == "__main__":
    unittest.main()
