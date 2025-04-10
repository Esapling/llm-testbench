import unittest
from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    result = ""
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result


class TestStringXor(unittest.TestCase):
    def test_string_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')
        self.assertEqual(string_xor('111', '000'), '111')
        self.assertEqual(string_xor('1010', '0101'), '1111')
        self.assertEqual(string_xor('0000', '0000'), '0000')
        self.assertEqual(string_xor('1111', '1111'), '0000')
        self.assertEqual(string_xor('1', '0'), '1')
        self.assertEqual(string_xor('0', '1'), '1')


if __name__ == '__main__':
    unittest.main()