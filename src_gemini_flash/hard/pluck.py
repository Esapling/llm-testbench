import unittest


def pluck(items, keys):
    """
    Given a list of dictionaries and a list of keys, return a new list containing only the dictionaries with the given keys.
    """
    result = []
    for item in items:
        new_item = {}
        for key in keys:
            if key in item:
                new_item[key] = item[key]
        result.append(new_item)
    return result


class TestPluck(unittest.TestCase):
    def test_pluck(self):
        items = [{'a': 1, 'b': 2, 'c': 3}, {'a': 4, 'b': 5, 'c': 6}]
        self.assertEqual(pluck(items, ['a', 'c']), [{'a': 1, 'c': 3}, {'a': 4, 'c': 6}])
        self.assertEqual(pluck(items, ['b']), [{'b': 2}, {'b': 5}])
        self.assertEqual(pluck(items, ['x', 'y']), [{}, {}])
        self.assertEqual(pluck([], ['a']), [])
        self.assertEqual(pluck([{'a': 1, 'b': 2}, {'a': 3}], []), [{}, {}])
        self.assertEqual(pluck([{'a': 1, 'b': 2}, {'a': 3}], ['a', 'b', 'c']), [{'a': 1, 'b': 2}, {'a': 3}])


if __name__ == '__main__':
    unittest.main()