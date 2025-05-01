"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return '0'
    
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base
    
    return ''.join(reversed(digits))

import unittest

class TestChangeBase(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(change_base(8, 3), '22')
        self.assertEqual(change_base(8, 2), '1000')
        self.assertEqual(change_base(7, 2), '111')
        
    def test_zero(self):
        self.assertEqual(change_base(0, 2), '0')
        self.assertEqual(change_base(0, 8), '0')
        
    def test_decimal_to_binary(self):
        self.assertEqual(change_base(10, 2), '1010')
        self.assertEqual(change_base(15, 2), '1111')
        
    def test_decimal_to_octal(self):
        self.assertEqual(change_base(64, 8), '100')
        self.assertEqual(change_base(15, 8), '17')
        
    def test_other_bases(self):
        self.assertEqual(change_base(10, 3), '101')
        self.assertEqual(change_base(25, 6), '41')

if __name__ == "__main__":
    unittest.main()
