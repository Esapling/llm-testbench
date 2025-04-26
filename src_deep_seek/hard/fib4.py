import unittest

def fib4(n: int):
    """ Compute the n-th element of the fib4 number sequence """
    if n == 0: return 0
    if n == 1: return 0
    if n == 2: return 2
    if n == 3: return 0
    
    a, b, c, d = 0, 0, 2, 0
    for _ in range(4, n+1):
        a, b, c, d = b, c, d, a + b + c + d
    return d

class TestFib4(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(fib4(5), 4)
    
    def test_example2(self):
        self.assertEqual(fib4(6), 8)
    
    def test_example3(self):
        self.assertEqual(fib4(7), 14)
    
    def test_base_cases(self):
        self.assertEqual(fib4(0), 0)
        self.assertEqual(fib4(1), 0)
        self.assertEqual(fib4(2), 2)
        self.assertEqual(fib4(3), 0)
    
    def test_larger_n(self):
        self.assertEqual(fib4(10), 104)

if __name__ == "__main__":
    unittest.main()