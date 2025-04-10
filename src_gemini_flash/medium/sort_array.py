import unittest


def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """

    if not array:
        return []

    new_array = array[:]  # Create a copy to not modify the original
    if (len(array) == 1) or ((array[0] + array[-1]) % 2 != 0):
        new_array.sort()
    else:
        new_array.sort(reverse=True)

    return new_array


class TestSortArray(unittest.TestCase):
    def test_sort_array(self):
        self.assertEqual(sort_array([]), [])
        self.assertEqual(sort_array([5]), [5])
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0])
        self.assertEqual(sort_array([1, 2, 3, 4]), [4, 3, 2, 1])
        self.assertEqual(sort_array([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()