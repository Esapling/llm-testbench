import unittest


def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.

    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    result = []
    for num in x:
        if not any(int(digit) % 2 == 0 for digit in str(num)):
            result.append(num)
    result.sort()
    return result


class TestUniqueDigits(unittest.TestCase):
    def test_unique_digits(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])
        self.assertEqual(unique_digits([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])
        self.assertEqual(unique_digits([2, 4, 6, 8, 10]), [])
        self.assertEqual(unique_digits([12, 14, 16, 18, 11]), [11])
        self.assertEqual(unique_digits([]), [])


if __name__ == '__main__':
    unittest.main()