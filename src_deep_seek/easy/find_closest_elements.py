from typing import List, Tuple
import unittest

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least 2 elements")
    
    sorted_nums = sorted(numbers)
    min_diff = float('inf')
    result = (sorted_nums[0], sorted_nums[1])
    
    for i in range(len(sorted_nums)-1):
        diff = sorted_nums[i+1] - sorted_nums[i]
        if diff < min_diff:
            min_diff = diff
            result = (sorted_nums[i], sorted_nums[i+1])
    
    return result

class TestFindClosestElements(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
    
    def test_duplicate_numbers(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))
    
    def test_negative_numbers(self):
        self.assertEqual(find_closest_elements([-1.5, -1.0, 0.0, 1.0]), (-1.5, -1.0))
    
    def test_large_numbers(self):
        self.assertEqual(find_closest_elements([100, 200, 300, 301]), (300, 301))
    
    def test_short_list(self):
        with self.assertRaises(ValueError):
            find_closest_elements([1.0])

if __name__ == "__main__":
    unittest.main()