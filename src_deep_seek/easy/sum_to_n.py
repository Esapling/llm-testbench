import unittest

def sum_to_n(n: int) -> int:
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    return n * (n + 1) // 2

class TestSumToN(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(sum_to_n(30), 465)
    
    def test_example2(self):
        self.assertEqual(sum_to_n(100), 5050)
    
    def test_small_number(self):
        self.assertEqual(sum_to_n(5), 15)
    
    def test_medium_number(self):
        self.assertEqual(sum_to_n(10), 55)
    
    def test_edge_case(self):
        self.assertEqual(sum_to_n(1), 1)

if __name__ == "__main__":
    unittest.main()