"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def compare_one(a, b):
    """ Returns the larger value between two variables of same type """
    if isinstance(a, str) and isinstance(b, str):
        a = a.replace(',', '.')
        b = b.replace(',', '.')
        a, b = float(a), float(b)

    if a == b:
        return None
    return max(a, b)

class Test(unittest.TestCase):
    def test_compare_one(self):
        self.assertEqual(compare_one(1, 2.5), 2.5)
        self.assertEqual(compare_one(1, "2,3"), "2,3")
        self.assertEqual(compare_one("5,1", "6"), "6")
        self.assertIsNone(compare_one("1", 1))

if __name__ == "__main__":
    unittest.main()
