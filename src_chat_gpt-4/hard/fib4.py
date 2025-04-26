def fib4(n: int):
    seq = [0, 0, 2, 0]
    if n < 4:
        return seq[n]
    for i in range(4, n + 1):
        seq.append(seq[-1] + seq[-2] + seq[-3] + seq[-4])
    return seq[n]

import unittest

class TestFib4(unittest.TestCase):
    def test_fib4_5(self):
        self.assertEqual(fib4(5), 4)
    def test_fib4_7(self):
        self.assertEqual(fib4(7), 14)