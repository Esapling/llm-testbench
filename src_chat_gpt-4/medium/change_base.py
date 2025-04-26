import unittest

def change_base(x: int, base: int) -> str:
    """ Change numerical base of input number x to base """
    if x == 0:
        return '0'
    digits = []
    while x:
        digits.append(str(x % base))
        x //= base
    return ''.join(digits[::-1])

class Test(unittest.TestCase):
    def test_change_base(self):
        self.assertEqual(change_base(8, 3), '22')
        self.assertEqual(change_base(8, 2), '1000')
        self.assertEqual(change_base(7, 2), '111')
        self.assertEqual(change_base(0, 2), '0')

if __name__ == "__main__":
    unittest.main()
