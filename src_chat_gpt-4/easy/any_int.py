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

if __name__ == "__main__":
    unittest.main()
