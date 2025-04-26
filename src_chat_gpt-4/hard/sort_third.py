def sort_third(l: list):
    idxs = [i for i in range(len(l)) if i % 3 == 0]
    vals = sorted(l[i] for i in idxs)
    for i, val in zip(idxs, vals):
        l[i] = val
    return l

import unittest

class TestSortThird(unittest.TestCase):
    def test_small(self):
        self.assertEqual(sort_third([1,2,3]), [1,2,3])
    def test_mix(self):
        self.assertEqual(sort_third([5,6,3,4,8,9,2]), [2,6,3,4,8,9,5])