"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
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

    # ----------- Phase 2 Tests -----------
    
    def test_large_numbers(self):
        self.assertEqual(change_base(1000000, 2), '11110100001001000000')
         
    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            change_base(-100, 5)
    
    def test_floating_point_input(self):
        with self.assertRaises(TypeError):
            change_base(10.5, 2)
        
    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            change_base("abc!", 6)
        with self.assertRaises(TypeError):
            change_base([10], 2)
       
    def test_zero_base(self):
        with self.assertRaises(ValueError):
            change_base(100, 0)
            
    def test_base_one(self):
        with self.assertRaises(ValueError):
            change_base(100, 1)
    

if __name__ == "__main__":
    unittest.main()