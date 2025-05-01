"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
from typing import List
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    mad = sum(abs(x - mean) for x in numbers) / len(numbers)
    return mad

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_examples(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)
        self.assertAlmostEqual(mean_absolute_deviation([1, 1, 1, 1]), 0.0)
    
    def test_negative_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([-2, -4, -6]), 1.3333333333333333)
    
    def test_mixed_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([-1, 0, 1]), 0.6666666666666666)

if __name__ == "__main__":
    unittest.main()
