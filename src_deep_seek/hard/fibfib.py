"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def fibfib(n: int):
    """ Compute the n-th element of the fibfib number sequence """
    if n == 0: return 0
    if n == 1: return 0
    if n == 2: return 1
    
    a, b, c = 0, 0, 1
    for _ in range(3, n+1):
        a, b, c = b, c, a + b + c
    return c

class TestFibFib(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(fibfib(1), 0)
    
    def test_example2(self):
        self.assertEqual(fibfib(5), 4)
    
    def test_example3(self):
        self.assertEqual(fibfib(8), 24)
    
    def test_base_cases(self):
        self.assertEqual(fibfib(0), 0)
        self.assertEqual(fibfib(2), 1)
    
    def test_larger_n(self):
        self.assertEqual(fibfib(10), 81)

if __name__ == "__main__":
    unittest.main()