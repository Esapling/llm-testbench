import unittest

def sort_third(l: list):
    """Sort elements at indices divisible by 3, keep others in place."""
    sorted_third = sorted([l[i] for i in range(len(l)) if i % 3 == 0])
    result = l[:]
    j = 0
    for i in range(len(l)):
        if i % 3 == 0:
            result[i] = sorted_third[j]
            j += 1
    return result

class Test(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
    def test_with_non_divisible(self):
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])
    def test_empty(self):
        self.assertEqual(sort_third([]), [])
    def test_large_list(self):
        self.assertEqual(sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == "__main__":
    unittest.main()
