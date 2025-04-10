import unittest


def sum_squares(nums):
    """
    Given a list of numbers, return the sum of their squares.
    sum_squares([1,2,3]) == 14
    sum_squares([1,2,3,4,5]) == 55
    sum_squares([1,-2,3]) == 14
    """
    return sum(x * x for x in nums)


class TestSumSquares(unittest.TestCase):
    def test_sum_squares(self):
        self.assertEqual(sum_squares([1, 2, 3]), 14)
        self.assertEqual(sum_squares([1, 2, 3, 4, 5]), 55)
        self.assertEqual(sum_squares([1, -2, 3]), 14)
        self.assertEqual(sum_squares([0, 0, 0]), 0)
        self.assertEqual(sum_squares([]), 0)
        self.assertEqual(sum_squares([-1, -2, -3]), 14)


if __name__ == '__main__':
    unittest.main()