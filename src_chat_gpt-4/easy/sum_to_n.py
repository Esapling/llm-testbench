
import unittest

def sum_to_n(n: int) -> int:
    return n * (n + 1) // 2

class TestSumToN(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sum_to_n(30), 465)
        self.assertEqual(sum_to_n(100), 5050)
    
    def test_small(self):
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(1), 1)

if __name__ == "__main__":
    unittest.main()
