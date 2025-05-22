"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""

import unittest

def any_int(x, y, z):
    if not all(isinstance(i, int) for i in (x, y, z)):
        return False
    return x + y == z or x + z == y or y + z == x

class TestAnyInt(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(any_int(5, 2, 7))
        self.assertFalse(any_int(3, 2, 2))
        self.assertTrue(any_int(3, -2, 1))
        self.assertFalse(any_int(3.6, -2.2, 2))
    
        #------------ Phase 2 Tests ------------
    
    def test_string_inputs(self):
        self.assertFalse(any_int("5", 2, 7))
    
    def test_boolean_values(self):
        self.assertFalse(any_int(True, False, 1))
        self.assertFalse(any_int(1, 0, True))
    
    def test_large_numbers(self):
        self.assertTrue(any_int(1000000, 2000000, 3000000))
        self.assertFalse(any_int(1000000, 2000000, 4000000))
        self.assertTrue(any_int(-1000000, -2000000, -3000000))
        self.assertFalse(any_int(-1000000, -2000000, -4000000))

    def test_all_zero(self):
        self.assertTrue(any_int(0, 0, 0))

if __name__ == "__main__":
    unittest.main()
