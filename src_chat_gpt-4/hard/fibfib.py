def fibfib(n: int):
    seq = [0, 0, 1]
    if n < 3:
        return seq[n]
    for i in range(3, n+1):
        seq.append(seq[-1] + seq[-2] + seq[-3])
    return seq[n]

import unittest

class TestFibFib(unittest.TestCase):
    def test_fibfib1(self):
        self.assertEqual(fibfib(1), 0)
    def test_fibfib5(self):
        self.assertEqual(fibfib(5), 4)
    def test_fibfib8(self):
        self.assertEqual(fibfib(8), 24)