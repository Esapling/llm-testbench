def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    if not lst:
        return 0
    
    result = 0
    
    for num in lst:
        # Check if the number is a positive odd integer
        if isinstance(num, (int, float)) and num > 0 and num.is_integer() and int(num) % 2 == 1:
            result += int(num) ** 2
    
    return result


# Unit tests
import unittest

class TestDoubleTheDifference(unittest.TestCase):
    def test_example_case_1(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)  # 1^2 + 3^2 = 1 + 9 = 10
    
    def test_example_case_2(self):
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)  # No positive odd integers
    
    def test_example_case_3(self):
        self.assertEqual(double_the_difference([9, -2]), 81)  # 9^2 = 81
    
    def test_example_case_4(self):
        self.assertEqual(double_the_difference([0]), 0)  # No positive odd integers
    
    def test_empty_list(self):
        self.assertEqual(double_the_difference([]), 0)
    
    def test_float_values(self):
        self.assertEqual(double_the_difference([1.0, 3.0, 2.5, 4.75]), 10)  # 1.0^2 + 3.0^2 = 1 + 9 = 10 (2.5 and 4.75 are not integers)
    
    def test_mixed_values(self):
        self.assertEqual(double_the_difference([5, -5, 5.0, 5.5, "5"]), 25)  # Only 5 and 5.0 are valid: 5^2 = 25
    
    def test_non_integer_floats(self):
        self.assertEqual(double_the_difference([1.5, 2.5, 3.5]), 0)  # None are integers

if __name__ == "__main__":
    unittest.main()
