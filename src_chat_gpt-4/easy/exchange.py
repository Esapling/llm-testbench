"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def exchange(lst1, lst2):
    has_even = any(x % 2 == 0 for x in lst2)
    if not has_even:
        return "NO"
    return "YES"

class TestExchange(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

    def test_all_even_in_lst2(self):
        self.assertEqual(exchange([1,3,5], [2,4,6]), "YES")

    #------------ Phase 2 Tests ------------
        
    def test_zero_in_lst1(self):
        self.assertEqual(exchange([0, 5, 4], [1, 3, 5]), "NO")
    
    def test_all_even_in_lst1(self):
        self.assertEqual(exchange([0, 2, 4], [1, 3, 5]), "YES")
        
    def test_all_odd_in_lst1(self):
        self.assertEqual(exchange([1, 3, 5], [9, 5, 6]), "NO")
        self.assertEqual(exchange([1, 3, 5], [10, 8, 16]), "YES")
        
    def test_with_different_lengths(self):
        self.assertEqual(exchange([1, 2], [3, 4, 5]), "YES")
        self.assertEqual(exchange([1, 2, 3], [11]), "NO")
    
    def test_no_evens_in_lst2(self):
        self.assertEqual(exchange([1, 3, 5], [7, 9, 11]), "NO")
    
    def test_negative_numbers(self):
        self.assertEqual(exchange([-1, -2, -3], [-41, -5, -61]), "NO")
        self.assertEqual(exchange([-1, -2, -3], [-4, -5, -6]), "YES")
        
    def test_with_non_integer(self):
        self.assertRaises(TypeError, exchange, [1.5, 2.5], [3.5, 4.5])
        self.assertRaises(TypeError, exchange, [False, 2.5], [3.5, True])

if __name__ == "__main__":
    unittest.main()
