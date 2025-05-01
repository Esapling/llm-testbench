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

if __name__ == "__main__":
    unittest.main()
