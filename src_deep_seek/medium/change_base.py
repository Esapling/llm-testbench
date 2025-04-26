import unittest

def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base."""
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9")
    if x == 0:
        return "0"
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x = x // base
    return ''.join(reversed(digits))

class TestChangeBase(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(change_base(8, 3), '22')
    
    def test_example2(self):
        self.assertEqual(change_base(8, 2), '1000')
    
    def test_example3(self):
        self.assertEqual(change_base(7, 2), '111')
    
    def test_zero(self):
        self.assertEqual(change_base(0, 2), '0')
    
    def test_invalid_base(self):
        with self.assertRaises(ValueError):
            change_base(10, 11)

if __name__ == "__main__":
    unittest.main()