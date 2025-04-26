
from typing import List, Tuple
import unittest

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers = sorted(numbers)
    closest = (numbers[0], numbers[1])
    min_diff = abs(numbers[1] - numbers[0])
    for i in range(1, len(numbers) - 1):
        diff = abs(numbers[i + 1] - numbers[i])
        if diff < min_diff:
            min_diff = diff
            closest = (numbers[i], numbers[i + 1])
    return closest

class TestFindClosestElements(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))

    def test_negatives(self):
        self.assertEqual(find_closest_elements([-2, -1, 0, 1]), (-1, 0))

    def test_unsorted(self):
        self.assertEqual(find_closest_elements([10, 1, 5, 7, 6]), (5, 6))

if __name__ == "__main__":
    unittest.main()
