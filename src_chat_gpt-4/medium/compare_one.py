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

    # ---------- Phase 2 Tests ----------
    
    def test_phase_invalid_input(self):
        with self.assertRaises(ValueError):
            compare_one("invalid", 1)
        with self.assertRaises(ValueError):
            compare_one(1, "invalid")
        with self.assertRaises(ValueError):
            compare_one("1,2,3", "4,5,6")
        with self.assertRaises(ValueError):
            compare_one("1.2.3", 1.2)
        
    def test_empty_strings(self):
        self.assertEqual(compare_one("", ""), None)
        self.assertEqual(compare_one("", 5), 5)
        
    def test_dot_comma_type_mixed(self):
        self.assertEqual(compare_one("0", 0), None)
        self.assertEqual(compare_one("1,000", "1000"), "1000")
        self.assertEqual(compare_one("1.000", 1050), 1050)
        self.assertEqual(compare_one("1.000", "1000"), "1000")
        self.assertEqual(compare_one(1234.56, "1234.56"), None)
        self.assertEqual(compare_one("1,234,567", "1234567"), None)


if __name__ == "__main__":
    unittest.main()
