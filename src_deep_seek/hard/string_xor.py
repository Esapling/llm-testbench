"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR on these inputs and return result as a string """
    return ''.join('1' if x != y else '0' for x, y in zip(a, b))

class TestStringXor(unittest.TestCase):
    def test_example(self):
        self.assertEqual(string_xor('010', '110'), '100')
    
    def test_same_input(self):
        self.assertEqual(string_xor('1010', '1010'), '0000')
    
    def test_different_length(self):
        with self.assertRaises(ValueError):
            string_xor('101', '1010')
    
    def test_all_ones(self):
        self.assertEqual(string_xor('1111', '1111'), '0000')
    
    def test_mixed_case(self):
        self.assertEqual(string_xor('0011', '0101'), '0110')

if __name__ == "__main__":
    unittest.main()