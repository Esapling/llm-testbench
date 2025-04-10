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
        return 0.0  # Handle empty list case

    mean = sum(numbers) / len(numbers)
    absolute_differences = [abs(x - mean) for x in numbers]
    mad = sum(absolute_differences) / len(absolute_differences)
    return mad


# Unit Tests
class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)
        self.assertEqual(mean_absolute_deviation([2.0, 2.0, 2.0, 2.0]), 0.0)
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]), 1.2)
        self.assertEqual(mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0, -5.0]), 1.2)
        self.assertEqual(mean_absolute_deviation([]), 0.0)


if __name__ == '__main__':
    unittest.main()