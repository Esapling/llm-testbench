import unittest

def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    """
    def parse_value(x):
        if isinstance(x, (int, float)):
            return x
        try:
            return float(x.replace(',', '.'))
        except:
            return None
    
    val_a = parse_value(a)
    val_b = parse_value(b)
    
    if val_a is None or val_b is None:
        return None
    
    if val_a > val_b:
        return a
    elif val_b > val_a:
        return b
    else:
        return None

class TestCompareOne(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(compare_one(1, 2.5), 2.5)
    
    def test_example2(self):
        self.assertEqual(compare_one(1, "2,3"), "2,3")
    
    def test_example3(self):
        self.assertEqual(compare_one("5,1", "6"), "6")
    
    def test_example4(self):
        self.assertIsNone(compare_one("1", 1))
    
    def test_equal_floats(self):
        self.assertIsNone(compare_one(3.14, 3.14))
    
    def test_invalid_string(self):
        self.assertIsNone(compare_one("abc", 1))

if __name__ == "__main__":
    unittest.main()