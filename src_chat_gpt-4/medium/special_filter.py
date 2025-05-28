"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def specialFilter(nums):
    """ Return the number of elements greater than 10 where both first and last digits are odd """
    def first_last_odd(n):
        str_n = str(abs(n))
        return int(str_n[0]) % 2 == 1 and int(str_n[-1]) % 2 == 1

    return sum(1 for num in nums if num > 10 and first_last_odd(num))

class Test(unittest.TestCase):
    def test_specialFilter(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)
        self.assertEqual(specialFilter([12, 24, 35, 51]), 2)
        self.assertEqual(specialFilter([15, 25, 35]), 2)
        
    # ------------- Phase 2 Tests -------------
    
    def test_empty_list(self):
        """ Test with an empty list """
        self.assertEqual(specialFilter([]), 0)
        
    def test_single_element(self):
        """ Test with a single element that meets the criteria """
        self.assertEqual(specialFilter([11]), 1)
        self.assertEqual(specialFilter([12]), 0)
        
    def test_less_than_ten(self):
        """ Test with elements less than or equal to 10 """
        self.assertEqual(specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 0)
        
    def test_greater_than_ten_all_odd(self):
        """ Test with all elements greater than 10 and both first and last digits odd """
        self.assertEqual(specialFilter([11, 13, 15, 17, 19]), 5)
        self.assertEqual(specialFilter([31, 53, 75, 97]), 4)
        
    def test_all_invalid_elements(self):
        """ Test with all elements not meeting the criteria """
        self.assertEqual(specialFilter([2, 4, 6, -11, -13, -15, -8, 10, 16]), 0)
        
    def test_large_elements(self):
        """ Test with large numbers to ensure correctness """
        self.assertEqual(specialFilter([100000000, 999999, 888888]), 1)
        
    
if __name__ == "__main__":
    unittest.main()
