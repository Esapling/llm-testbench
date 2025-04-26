def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """
    # Count the number of odd numbers in lst1
    odd_in_lst1 = sum(1 for num in lst1 if num % 2 != 0)
    
    # Count the number of even numbers in lst2
    even_in_lst2 = sum(1 for num in lst2 if num % 2 == 0)
    
    # If we can replace all odd numbers in lst1 with even numbers from lst2, return "YES"
    return "YES" if odd_in_lst1 <= even_in_lst2 else "NO"


# Unit tests
import unittest

class TestExchange(unittest.TestCase):
    def test_example_case_1(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")
    
    def test_example_case_2(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")
    
    def test_all_even_in_lst1(self):
        self.assertEqual(exchange([2, 4, 6, 8], [1, 3, 5, 7]), "YES")
    
    def test_all_odd_in_lst1_enough_even_in_lst2(self):
        self.assertEqual(exchange([1, 3, 5, 7], [2, 4, 6, 8]), "YES")
    
    def test_all_odd_in_lst1_not_enough_even_in_lst2(self):
        self.assertEqual(exchange([1, 3, 5, 7], [2, 4, 1, 3]), "NO")
    
    def test_mixed_with_exact_match(self):
        self.assertEqual(exchange([1, 2, 3, 4], [5, 6, 7, 8]), "YES")
    
    def test_minimal_lists(self):
        self.assertEqual(exchange([1], [2]), "YES")
        self.assertEqual(exchange([1], [3]), "NO")
    
    def test_odd_numbers_in_lst2_dont_matter(self):
        self.assertEqual(exchange([1, 3], [5, 7, 2, 4]), "YES")

if __name__ == "__main__":
    unittest.main()
