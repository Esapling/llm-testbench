"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
from typing import List
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    if not numbers:
        return 0.0
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_basic_case(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)
    
    def test_three_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([10.0, 20.0, 30.0]), 20/3)
    
    def test_single_number(self):
        self.assertEqual(mean_absolute_deviation([5.0]), 0.0)
    
    def test_negative_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([-1.0, 0.0, 1.0]), 2/3)
    
    def test_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)

        #------------ Phase 2 Tests --------------------------------
    # def test_empty_list(self):
    #     self.assertEqual(mean_absolute_deviation([]), 0.0)

    # def test_single_element(self):
    #     self.assertEqual(mean_absolute_deviation([5]), 0.0)
    #     self.assertEqual(mean_absolute_deviation([-20]), 0.0)
    
    def test_identical_elements(self):
        self.assertEqual(mean_absolute_deviation([7, 7, 7]), 0.0)
        self.assertEqual(mean_absolute_deviation([3.5, 3.5, 3.5]), 0.0)

    def test_large_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([1000000, 2000000, 3000000]),666666.6666666666)
    
    def test_small_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([0.0001, 0.0002, 0.0003]),6.666666666666666e-05)
    def test_very_large_list(self):
        large_list = [i for i in range(1000000)]
        self.assertAlmostEqual(mean_absolute_deviation(large_list), 250000.0)

    def test_floating_point_precision(self):
        self.assertAlmostEqual(mean_absolute_deviation([0.1, 0.2, 0.3]),0.06666666666666667)
        self.assertAlmostEqual(mean_absolute_deviation([0.123456789, 0.987654321]),0.432098766)    

if __name__ == "__main__":
    unittest.main()