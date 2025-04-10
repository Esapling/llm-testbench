import unittest


def double_the_difference(nums):
    """
    Given a list of numbers, replace each number with twice the difference
    between the largest and the smallest number.
    double_the_difference([1, 2, 3]) == [4, 2, 0]
    double_the_difference([5, 1, 7, 2]) == [4, 12, 0, 10]
    double_the_difference([10, 10, 10]) == [0, 0, 0]
    """
    if not nums:
        return []
    largest = max(nums)
    smallest = min(nums)
    diff = largest - smallest
    return [2 * (diff - num + smallest) for num in nums]


class TestDoubleTheDifference(unittest.TestCase):
    def test_double_the_difference(self):
        self.assertEqual(double_the_difference([1, 2, 3]), [4, 2, 0])
        self.assertEqual(double_the_difference([5, 1, 7, 2]), [4, 12, 0, 10])
        self.assertEqual(double_the_difference([10, 10, 10]), [0, 0, 0])
        self.assertEqual(double_the_difference([5]), [0])
        self.assertEqual(double_the_difference([]), [])
        self.assertEqual(double_the_difference([-1, -2, -3]), [4, 2, 0])


if __name__ == '__main__':
    unittest.main()