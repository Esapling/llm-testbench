"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    """
    count_odd_lst1 = sum(1 for num in lst1 if num % 2 != 0)
    count_even_lst2 = sum(1 for num in lst2 if num % 2 == 0)
    return "YES" if count_even_lst2 >= count_odd_lst1 else "NO"

class TestExchange(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")
    
    def test_example2(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")
    
    def test_all_odd_with_enough_evens(self):
        self.assertEqual(exchange([1, 3, 5], [2, 4, 6]), "YES")
    
    def test_not_enough_evens(self):
        self.assertEqual(exchange([1, 1, 1], [2, 2]), "NO")
    
    def test_already_all_even(self):
        self.assertEqual(exchange([2, 4, 6], [1, 3, 5]), "YES")

if __name__ == "__main__":
    unittest.main()