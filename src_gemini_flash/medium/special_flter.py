import unittest


def specialFilter(x):
    """
    Given a list of strings, return a list of strings that contain only digits.
    """
    return list(filter(lambda s: s.isdigit(), x))


class TestSpecialFilter(unittest.TestCase):
    def test_specialFilter(self):
        self.assertEqual(specialFilter(["123", "abc", "456"]), ["123", "456"])
        self.assertEqual(specialFilter(["abc", "def"]), [])
        self.assertEqual(specialFilter(["123", "456", "789"]), ["123", "456", "789"])
        self.assertEqual(specialFilter(["12a", "12", "a12"]), ["12"])
        self.assertEqual(specialFilter([], []), [])


if __name__ == '__main__':
    unittest.main()