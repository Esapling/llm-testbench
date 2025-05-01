"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

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

    result = ""
    # The base numbers are less than 10, so digits will be 0-9, which are
    # directly representable as strings.
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x //= base

    return result

class TestChangeBase(unittest.TestCase):

    def test_example_1(self):
        """Test the first example case."""
        self.assertEqual(change_base(8, 3), '22')

    def test_example_2(self):
        """Test the second example case."""
        self.assertEqual(change_base(8, 2), '1000')

    def test_example_3(self):
        """Test the third example case."""
        self.assertEqual(change_base(7, 2), '111')

    def test_zero_input(self):
        """Test with input x as 0."""
        self.assertEqual(change_base(0, 2), '0')
        self.assertEqual(change_base(0, 8), '0')

    def test_larger_number_different_base(self):
        """Test with a larger number and a different base (e.g., base 8)."""
        self.assertEqual(change_base(100, 8), '144') # 1*8^2 + 4*8^1 + 4*8^0 = 64 + 32 + 4 = 100
        self.assertEqual(change_base(27, 3), '1000') # 1*3^3 + 0*3^2 + 0*3^1 + 0*3^0 = 27


# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)