import math

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    """
    # Round each number to ceiling and square it
    ceil_squared = [math.ceil(num) ** 2 for num in lst]
    
    # Return the sum
    return sum(ceil_squared)


# Unit tests
import unittest

class TestSumSquares(unittest.TestCase):
    def test_example_case_1(self):
        self.assertEqual(sum_squares([1, 2, 3]), 14)  # 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14
    
    def test_example_case_2(self):
        self.assertEqual(sum_squares([1, 4, 9]), 98)  # 1^2 + 4^2 + 9^2 = 1 + 16 + 81 = 98
    
    def test_example_case_3(self):
        self.assertEqual(sum_squares([1, 3, 5, 7]), 84)  # 1^2 + 3^2 + 5^2 + 7^2 = 1 + 9 + 25 + 49 = 84
    
    def test_example_case_4(self):
        self.assertEqual(sum_squares([1.4, 4.2, 0]), 29)  # ceil(1.4)^2 + ceil(4.2)^2 + ceil(0)^2 = 2^2 + 5^2 + 0^2 = 4 + 25 + 0 = 29
    
    def test_example_case_5(self):
        self.assertEqual(sum_squares([-2.4, 1, 1]), 6)  # ceil(-2.4)^2 + 1^2 + 1^2 = (-2)^2 + 1 + 1 = 4 + 2 = 6
    
    def test_empty_list(self):
        self.assertEqual(sum_squares([]), 0)
    
    def test_large_decimal(self):
        self.assertEqual(sum_squares([3.999, 5.001]), 34)  # ceil(3.999)^2 + ceil(5.001)^2 = 4^2 + 6^2 = 16 + 36 = 52
    
    def test_large_negative(self):
        self.assertEqual(sum_squares([-10.9]), 100)  # ceil(-10.9)^2 = (-10)^2 = 100

if __name__ == "__main__":
    unittest.main()
