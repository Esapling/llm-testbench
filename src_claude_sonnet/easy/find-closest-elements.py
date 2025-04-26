from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")
    
    # Initialize with the first two elements
    sorted_pair = (min(numbers[0], numbers[1]), max(numbers[0], numbers[1]))
    min_diff = abs(numbers[0] - numbers[1])
    
    # Check all possible pairs
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            
            # If we found a smaller difference
            if diff < min_diff:
                min_diff = diff
                sorted_pair = (min(numbers[i], numbers[j]), max(numbers[i], numbers[j]))
            # If we found equal difference, maintain order
            elif diff == min_diff:
                if min(numbers[i], numbers[j]) < sorted_pair[0]:
                    sorted_pair = (min(numbers[i], numbers[j]), max(numbers[i], numbers[j]))
    
    return sorted_pair


# Unit tests
import unittest

class TestFindClosestElements(unittest.TestCase):
    def test_example_case_1(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
    
    def test_example_case_2(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))
    
    def test_identical_elements(self):
        self.assertEqual(find_closest_elements([5.0, 5.0, 8.0, 10.0]), (5.0, 5.0))
    
    def test_negative_elements(self):
        self.assertEqual(find_closest_elements([-10.0, -9.8, 5.0, 20.0]), (-10.0, -9.8))
    
    def test_minimal_list(self):
        self.assertEqual(find_closest_elements([3.5, 2.0]), (2.0, 3.5))
    
    def test_multiple_equal_differences(self):
        # Both (1,2) and (3,4) have difference 1, but (1,2) comes first in sorted order
        self.assertEqual(find_closest_elements([1.0, 3.0, 4.0, 2.0]), (1.0, 2.0))
    
    def test_too_short_list(self):
        with self.assertRaises(ValueError):
            find_closest_elements([1.0])

if __name__ == "__main__":
    unittest.main()
