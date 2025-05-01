"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
def sum_to_n(n: int):
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
    # We can use the arithmetic series formula: sum = n(n+1)/2
    return n * (n + 1) // 2


# Unit tests
import unittest

class TestSumToN(unittest.TestCase):
    def test_example_case_30(self):
        self.assertEqual(sum_to_n(30), 465)
    
    def test_example_case_100(self):
        self.assertEqual(sum_to_n(100), 5050)
    
    def test_example_case_5(self):
        self.assertEqual(sum_to_n(5), 15)
    
    def test_example_case_10(self):
        self.assertEqual(sum_to_n(10), 55)
    
    def test_example_case_1(self):
        self.assertEqual(sum_to_n(1), 1)
    
    def test_zero(self):
        self.assertEqual(sum_to_n(0), 0)
    
    def test_negative(self):
        # For negative numbers, return 0 or raise an exception depending on requirements
        # This test assumes returning 0 for negative inputs
        self.assertEqual(sum_to_n(-5), 0)  # Alternatively, could raise an exception

if __name__ == "__main__":
    unittest.main()
