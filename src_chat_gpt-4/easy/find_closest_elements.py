"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
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

    #------------ Phase 2 Tests ------------
    
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_closest_elements([])
    
    def test_single_element(self):
        with self.assertRaises(ValueError):
            find_closest_elements([1.0])
    
    def test_minimal_list(self):
        self.assertEqual(find_closest_elements([3.5, 2.0]), (2.0, 3.5))
        
    def test_identical_elements(self):
        self.assertEqual(find_closest_elements([5.0, 5.0, 8.0, 10.0]), (5.0, 5.0))
        
    def test_large_numbers(self):
        self.assertEqual(find_closest_elements([1000000, 1000001, 1000002]), (1000000, 1000001))
       
    def test_not_enough_numeric(self):
        with self.assertRaises(TypeError):
            find_closest_elements([1, "a"])
        with self.assertRaises(TypeError):
            find_closest_elements(["b", 'a', "cat", "dog"])

    def test_mixed_types(self):
        self.assertEqual(find_closest_elements([1, "a", 3]), (1, 3))

    
if __name__ == "__main__":
    unittest.main()
