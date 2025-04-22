import unittest
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return ""YES"".
    Otherwise, return ""NO"".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => ""YES""
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => ""NO""
    It is assumed that the input lists will be non-empty.
    """
    odd_count_lst1 = sum(1 for x in lst1 if x % 2 != 0)
    even_count_lst2 = sum(1 for x in lst2 if x % 2 == 0)

    if odd_count_lst1 <= even_count_lst2:
        return "YES"
    else:
        return "NO"

class TestExchange(unittest.TestCase):

    def test_example_1(self):
        """Test the first example case."""
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")

    def test_example_2(self):
        """Test the second example case."""
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

    def test_exchange_possible(self):
        """Test case where lst1 needs odd numbers replaced and lst2 has enough evens."""
        self.assertEqual(exchange([1, 3, 5], [2, 4, 6]), "YES")
        self.assertEqual(exchange([1, 3], [2, 4, 6, 8]), "YES")


    def test_exchange_not_possible(self):
        """Test case where lst1 needs odd numbers replaced but lst2 doesn't have enough evens."""
        self.assertEqual(exchange([1, 3, 5], [2, 4]), "NO")
        self.assertEqual(exchange([1, 1, 1, 1], [2, 2, 2]), "NO")


    def test_lst1_already_even(self):
        """Test case where lst1 already contains only even numbers."""
        self.assertEqual(exchange([2, 4, 6], [1, 3, 5]), "YES")
        self.assertEqual(exchange([0, 2, 8], [1, 3, 5, 7]), "YES")


# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)