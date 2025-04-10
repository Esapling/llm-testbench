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
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base
    return ''.join(digits[::-1])


class TestChangeBase(unittest.TestCase):
    def test_change_base(self):
        self.assertEqual(change_base(8, 3), '22')
        self.assertEqual(change_base(8, 2), '1000')
        self.assertEqual(change_base(7, 2), '111')
        self.assertEqual(change_base(10, 10), '10')
        self.assertEqual(change_base(0, 2), '0')
        self.assertEqual(change_base(15, 2), '1111')


if __name__ == '__main__':
    unittest.main()