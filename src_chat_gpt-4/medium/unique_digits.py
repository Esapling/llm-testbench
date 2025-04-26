import unittest

def unique_digits(x):
    """ Given a list of positive integers x, return a sorted list of all elements that haven't any even digit """
    def has_even_digit(n):
        return any(int(digit) % 2 == 0 for digit in str(n))

    return sorted([n for n in x if not has_even_digit(n)])

class Test(unittest.TestCase):
    def test_unique_digits(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])
        self.assertEqual(unique_digits([1, 5, 7, 9]), [1, 5, 7, 9])
        self.assertEqual(unique_digits([11, 13, 17, 19]), [11, 13, 17, 19])

if __name__ == "__main__":
    unittest.main()
