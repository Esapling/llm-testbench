import unittest

def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    if n < 0:
        # The problem implies positive n based on examples, but a more
        # general approach might define sum up to a negative number.
        # Sticking to the prompt's implication of non-negative n for now.
        # If n is 0, the sum from 1 to 0 is an empty sum, which is 0.
        return 0
    
    # Using the formula for the sum of an arithmetic series
    return n * (n + 1) // 2

class TestSumToN(unittest.TestCase):

    def test_example_30(self):
        """Test the example case n = 30."""
        self.assertEqual(sum_to_n(30), 465)

    def test_example_100(self):
        """Test the example case n = 100."""
        self.assertEqual(sum_to_n(100), 5050)

    def test_examples_5_and_10(self):
        """Test the example cases n = 5 and n = 10."""
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(10), 55)

    def test_example_1(self):
        """Test the example case n = 1."""
        self.assertEqual(sum_to_n(1), 1)

    def test_n_is_zero(self):
        """Test the case when n is 0."""
        self.assertEqual(sum_to_n(0), 0)

# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)