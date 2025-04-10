import unittest


def compare_one(str1, str2):
    """
    Given two strings, return the number of positions where they contain the same length 1 substring.
    """
    count = 0
    shorter_len = min(len(str1), len(str2))
    for i in range(shorter_len - 1):
        if str1[i:i+2] == str2[i:i+2]:
            count += 1
    return count


class TestCompareOne(unittest.TestCase):
    def test_compare_one(self):
        self.assertEqual(compare_one("aa", "bb"), 0)
        self.assertEqual(compare_one("aa", "aaa"), 1)
        self.assertEqual(compare_one("abc", "abc"), 2)
        self.assertEqual(compare_one("abc", "axc"), 1)
        self.assertEqual(compare_one("abcd", "abcd"), 3)
        self.assertEqual(compare_one("abcd", "abxd"), 2)
        self.assertEqual(compare_one("ab", "abc"), 1)
        self.assertEqual(compare_one("a", "b"), 0)
        self.assertEqual(compare_one("", ""), 0)


if __name__ == '__main__':
    unittest.main()