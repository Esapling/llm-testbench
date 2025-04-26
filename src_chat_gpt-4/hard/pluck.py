import unittest

def pluck(arr):
    """Pluck the smallest even value from the list."""
    even_vals = [(val, idx) for idx, val in enumerate(arr) if val % 2 == 0]
    if not even_vals:
        return []
    return min(even_vals, key=lambda x: (x[0], x[1]))

class Test(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(pluck([4, 2, 3]), [2, 1])
    def test_with_zero(self):
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])
    def test_no_even(self):
        self.assertEqual(pluck([1, 3, 5]), [])
    def test_empty(self):
        self.assertEqual(pluck([]), [])

if __name__ == "__main__":
    unittest.main()
