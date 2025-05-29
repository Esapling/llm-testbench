"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit."""
    def has_even_digit(n):
        for digit in str(n):
            if int(digit) % 2 == 0:
                return True
        return False
    
    result = [num for num in x if not has_even_digit(num)]
    result.sort()
    return result

class TestUniqueDigits(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
    
    def test_example2(self):
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])
    
    def test_all_odd(self):
        self.assertEqual(unique_digits([135, 357, 579]), [135, 357, 579])
    
    def test_all_even(self):
        self.assertEqual(unique_digits([246, 468, 802]), [])
    
    def test_mixed(self):
        self.assertEqual(unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 3, 5, 7, 9])

    # ------------- Phase 2 Tests -------------

    def test_large_numbers(self):
        self.assertEqual(unique_digits([1357913579]), [1357913579])
        self.assertEqual(unique_digits([999999999]), [999999999])
        
    def test_sorting_order(self):
        self.assertEqual(unique_digits([97, 13, 755, 31, 1]), [1, 13, 31, 97, 755])
        self.assertEqual(unique_digits([99, 77, 55, 33, 11]), [11, 33, 55, 77, 99])
        
    def test_empty_list(self):
        self.assertEqual(unique_digits([]), [])


if __name__ == "__main__":
    unittest.main()
    