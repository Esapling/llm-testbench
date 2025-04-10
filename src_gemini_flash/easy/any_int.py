import unittest


def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.

    Examples
    any_int(5, 2, 7) ➞ True

    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True

    any_int(3.6, -2.2, 2) ➞ False

    '''
    if not all(isinstance(i, int) for i in [x, y, z]):
        return False

    return (x == y + z) or (y == x + z) or (z == x + y)


class TestAnyInt(unittest.TestCase):
    def test_any_int(self):
        self.assertEqual(any_int(5, 2, 7), True)
        self.assertEqual(any_int(3, 2, 2), False)
        self.assertEqual(any_int(3, -2, 1), True)
        self.assertEqual(any_int(3.6, -2.2, 2), False)
        self.assertEqual(any_int(0, 0, 0), True)
        self.assertEqual(any_int(1, 1, 2), True)
        self.assertEqual(any_int(-1, -1, -2), True)
        self.assertEqual(any_int(1, 2, 3.0), False)


if __name__ == '__main__':
    unittest.main()