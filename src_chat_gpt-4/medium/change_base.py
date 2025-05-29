"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
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
        
    # ----------- Phase 2 Tests -----------
    
    def test_large_numbers(self):
        self.assertEqual(change_base(1000000, 2), '11110100001001000000')

    def test_invalid_base(self):
        with self.assertRaises(ValueError):
            change_base(10, 37)
        with self.assertRaises(ValueError):
            change_base(10, -2)
        
    '''   
    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            change_base(-100, 5)
    
    '''   
    
    def test_floating_point_input(self):
        with self.assertRaises(TypeError):
            change_base(10.5, 2)
        
    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            change_base("100", 10)
        with self.assertRaises(TypeError):
            change_base([10], 2)
       
    def test_zero_base(self):
        with self.assertRaises(ValueError):
            change_base(100, 0)
    '''   
    def test_base_one(self):
        with self.assertRaises(ValueError):
            change_base(100, 1)
    '''   
if __name__ == "__main__":
    unittest.main()
