from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    if not numbers:
        return 0.0
    
    # Calculate mean of the dataset
    mean = sum(numbers) / len(numbers)
    
    # Calculate absolute deviations
    absolute_deviations = [abs(x - mean) for x in numbers]
    
    # Calculate mean of absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)
    
    return mad


# Unit tests
import unittest

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)
    
    def test_single_element(self):
        self.assertEqual(mean_absolute_deviation([5.0]), 0.0)
    
    def test_same_elements(self):
        self.assertEqual(mean_absolute_deviation([2.0, 2.0, 2.0]), 0.0)
    
    def test_negative_elements(self):
        self.assertAlmostEqual(mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0]), 1.0)
    
    def test_mixed_elements(self):
        self.assertEqual(mean_absolute_deviation([-10.0, 0.0, 10.0]), 6.666666666666667)
    
    def test_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)

if __name__ == "__main__":
    unittest.main()
