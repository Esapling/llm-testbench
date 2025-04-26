def string_xor(a: str, b: str) -> str:
    return ''.join('1' if x != y else '0' for x, y in zip(a, b))

import unittest

class TestStringXor(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(string_xor('010', '110'), '100')
    def test_all_same(self):
        self.assertEqual(string_xor('111', '111'), '000')
    def test_all_different(self):
        self.assertEqual(string_xor('000', '111'), '111')