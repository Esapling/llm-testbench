"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    
    for num in nums:
        # Check if number is greater than 10
        if num > 10:
            # Convert to string to get first and last digits
            num_str = str(abs(num))
            first_digit = int(num_str[0])
            last_digit = int(num_str[-1])
            
            # Check if both first and last digits are odd
            if first_digit % 2 == 1 and last_digit % 2 == 1:
                count += 1
    
    return count

import unittest

class TestSpecialFilter(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)
        
    def test_empty_array(self):
        self.assertEqual(specialFilter([]), 0)
        
    def test_no_matches(self):
        self.assertEqual(specialFilter([2, 4, 6, 8, 10]), 0)
        self.assertEqual(specialFilter([12, 24, 36, 48]), 0)
        
    def test_all_matches(self):
        self.assertEqual(specialFilter([15, 35, 57, 79, 99]), 5)
        
    def test_negative_numbers(self):
        self.assertEqual(specialFilter([-15, -35, -57]), 0)  # Not greater than 10
        
    def test_border_cases(self):
        self.assertEqual(specialFilter([9, 10, 11]), 1)  # Only 11 meets criteria
        
    def test_large_numbers(self):
        self.assertEqual(specialFilter([111, 222, 333, 444, 555]), 3)  # 111, 333, 555 meet criteria

if __name__ == "__main__":
    unittest.main()
