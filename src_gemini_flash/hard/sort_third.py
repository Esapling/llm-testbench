import unittest


def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    third_indices_values = [l[i] for i in range(len(l)) if i % 3 == 0]
    third_indices_values.sort()

    result = []
    third_index_counter = 0
    for i in range(len(l)):
        if i % 3 == 0:
            result.append(third_indices_values[third_index_counter])
            third_index_counter += 1
        else:
            result.append(l[i])
    return result


class TestSortThird(unittest.TestCase):
    def test_sort_third(self):
        self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])
        self.assertEqual(sort_third([9, 6, 3, 4, 8, 5, 2]), [3, 6, 9, 4, 8, 5, 2])
        self.assertEqual(sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(sort_third([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        self.assertEqual(sort_third([]), [])


if __name__ == '__main__':
    unittest.main()