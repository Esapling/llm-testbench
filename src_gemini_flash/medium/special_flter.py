"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest
from typing import List

def specialFilter(nums: List[int]) -> int:
    """Write a function that takes an array of numbers as input and returns
    the number of elements in the array that are greater than 10 and both
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        # Check condition 1: number is greater than 10
        if num > 10:
            # Check condition 2: both first and last digits are odd
            str_num = str(abs(num)) # Use abs to handle negative numbers correctly for digit extraction
            first_digit = int(str_num[0])
            last_digit = int(str_num[-1])

            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count

class TestSpecialFilter(unittest.TestCase):

    def test_example_1(self):
        """Test the first example case."""
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)

    def test_example_2(self):
        """Test the second example case."""
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)

    def test_all_meet_criteria(self):
        """Test a list where all numbers meet the criteria."""
        self.assertEqual(specialFilter([11, 13, 15, 17, 19]), 5)
        self.assertEqual(specialFilter([31, 53, 75, 97]), 4)


    def test_none_meet_criteria(self):
        """Test a list where no numbers meet the criteria."""
        self.assertEqual(specialFilter([20, 30, 40, 10]), 0) # Numbers <= 10 or even last digit
        self.assertEqual(specialFilter([12, 14, 21, 43]), 0) # Even first or last digit
        self.assertEqual(specialFilter([-11, -13, -15]), 0) # Numbers <= 10


    def test_mixed_cases(self):
        """Test a mix of numbers meeting and not meeting the criteria."""
        self.assertEqual(specialFilter([11, 12, 21, 101, 110, 111]), 3) # 11, 101, 111 meet the criteria
        self.assertEqual(specialFilter([1, 10, 11, 20, 22, 33, 40, 44, 55]), 2) # 11, 33, 55 meet the criteria


# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)