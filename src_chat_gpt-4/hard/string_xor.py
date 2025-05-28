"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def string_xor(a: str, b: str) -> str:
    """Perform binary XOR on two strings of 1s and 0s."""
    return ''.join('0' if x == y else '1' for x, y in zip(a, b))

class Test(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(string_xor('010', '110'), '100')
    def test_same(self):
        self.assertEqual(string_xor('111', '111'), '000')
    def test_diff(self):
        self.assertEqual(string_xor('101', '010'), '111')
    def test_empty(self):
        self.assertEqual(string_xor('', ''), '')
        
    # ----------- Phase 2 Tests -----------
    
    def test_empty_strings(self):
        self.assertEqual(string_xor('', ''), '')
        self.assertEqual(string_xor('1010', ''), '1010')
        self.assertEqual(string_xor('', '1100'), '1100')
    
    def test_single_characters(self):
        self.assertEqual(string_xor('0', '1'), '1')
        self.assertEqual(string_xor('1', '0'), '1')
        self.assertEqual(string_xor('0', '0'), '0')
        self.assertEqual(string_xor('1', '1'), '0')
        
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
    
    

if __name__ == "__main__":
    unittest.main()
