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
        raise ValueError("List must contain at least two numbers")

    numbers.sort()  # Sort the numbers to easily find closest pairs
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[1])

    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair


# Unit Tests
class TestFindClosestElements(unittest.TestCase):
    def test_find_closest_elements(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))
        self.assertEqual(find_closest_elements([5.0, 4.0, 3.0, 2.0, 1.0]), (1.0, 2.0))
        self.assertEqual(find_closest_elements([-1.0, -2.0, -3.0, -4.0]), (-4.0, -3.0))
        self.assertEqual(find_closest_elements([1.1, 1.2, 1.3, 1.4]), (1.1, 1.2))
        with self.assertRaises(ValueError) as context:
            find_closest_elements([1.0])
        self.assertEqual(str(context.exception), "List must contain at least two numbers")


if __name__ == '__main__':
    unittest.main()