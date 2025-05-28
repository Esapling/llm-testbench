"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def fibfib(n: int):
    """Compute the n-th element of the fibfib sequence."""
    a, b, c = 0, 0, 1
    if n == 0:
        return a
    elif n == 1:
        return b
    elif n == 2:
        return c
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c

class Test(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(fibfib(1), 0)
    def test_example(self):
        self.assertEqual(fibfib(5), 4)
    def test_large(self):
        self.assertEqual(fibfib(8), 24)
    def test_zero(self):
        self.assertEqual(fibfib(0), 0)

    # -------------- Phase 2 Tests -------------
    
    def test_n_equals_3(self):
        self.assertEqual(fibfib(3), 1) 
    
    def test_large_n(self):
        self.assertEqual(fibfib(20), 35890)
    
    def test_negative_n(self):
        with self.assertRaises(IndexError):
            fibfib(-1)
            
    def test_non_integer_n(self):
        with self.assertRaises(TypeError):
            fibfib(5.5)
        with self.assertRaises(TypeError):
            fibfib("string")
        with self.assertRaises(TypeError):
            fibfib([1, 2, 3])
        with self.assertRaises(TypeError):
            fibfib(None)
            
    

if __name__ == "__main__":
    unittest.main()
