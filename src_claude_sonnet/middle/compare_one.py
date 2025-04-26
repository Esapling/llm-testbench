def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    # Convert to comparable values
    def convert_to_float(val):
        if isinstance(val, (int, float)):
            return float(val)
        elif isinstance(val, str):
            # Replace comma with dot for string representation of float
            return float(val.replace(',', '.'))
        return val
    
    a_val = convert_to_float(a)
    b_val = convert_to_float(b)
    
    # Compare and return the larger value in its original type
    if a_val == b_val:
        return None
    elif a_val > b_val:
        return a
    else:
        return b

import unittest

class TestCompareOne(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(compare_one(1, 2.5), 2.5)
        self.assertEqual(compare_one(1, "2,3"), "2,3")
        self.assertEqual(compare_one("5,1", "6"), "6")
        self.assertIsNone(compare_one("1", 1))
        
    def test_integers(self):
        self.assertEqual(compare_one(5, 10), 10)
        self.assertEqual(compare_one(20, 15), 20)
        self.assertIsNone(compare_one(7, 7))
        
    def test_floats(self):
        self.assertEqual(compare_one(3.14, 2.71), 3.14)
        self.assertEqual(compare_one(1.5, 2.5), 2.5)
        self.assertIsNone(compare_one(4.2, 4.2))
        
    def test_strings(self):
        self.assertEqual(compare_one("7,5", "3,2"), "7,5")
        self.assertEqual(compare_one("2.5", "10.1"), "10.1")
        self.assertIsNone(compare_one("5.0", "5,0"))
        
    def test_mixed_types(self):
        self.assertEqual(compare_one(10, "5,5"), 10)
        self.assertEqual(compare_one("15.5", 10), "15.5")
        self.assertEqual(compare_one(7.5, "10"), "10")

if __name__ == "__main__":
    unittest.main()
