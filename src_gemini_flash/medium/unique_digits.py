import unittest
from typing import List

def unique_digits(x: List[int]) -> List[int]:
    """Given a list of positive integers x. return a sorted list of all
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.

    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    result_list = []
    for num in x:
        has_even_digit = False
        # Convert number to string to check digits
        for digit_char in str(num):
            digit = int(digit_char)
            if digit % 2 == 0:
                has_even_digit = True
                break # Found an even digit, no need to check further for this number
        if not has_even_digit:
            result_list.append(num)

    # Sort the resulting list
    result_list.sort()

    return result_list

class TestUniqueDigits(unittest.TestCase):

    def test_example_1(self):
        """Test the first example case."""
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])

    def test_example_2_no_unique_digits(self):
        """Test the second example case where no numbers have only odd digits."""
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])

    def test_empty_list(self):
        """Test with an empty input list."""
        self.assertEqual(unique_digits([]), [])

    def test_all_only_odd_digits(self):
        """Test with a list where all numbers contain only odd digits."""
        self.assertEqual(unique_digits([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])
        self.assertEqual(unique_digits([11, 35, 79, 135]), [11, 35, 79, 135])

    def test_mixed_cases_with_duplicates(self):
        """Test with mixed valid/invalid numbers and duplicates."""
        self.assertEqual(unique_digits([13, 24, 57, 80, 91, 13]), [13, 13, 57, 91])
        self.assertEqual(unique_digits([22, 44, 11, 66, 33, 88]), [11, 33])


# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)