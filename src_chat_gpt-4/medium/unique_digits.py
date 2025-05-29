"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def unique_digits(x):
    """ Given a list of positive integers x, return a sorted list of all elements that haven't any even digit """
    def has_even_digit(n):
        return any(int(digit) % 2 == 0 for digit in str(n))

    return sorted([n for n in x if not has_even_digit(n)])

class Test(unittest.TestCase):
    def test_unique_digits(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])
        self.assertEqual(unique_digits([1, 5, 7, 9]), [1, 5, 7, 9])
        self.assertEqual(unique_digits([11, 13, 17, 19]), [11, 13, 17, 19])

    # ------------- Phase 2 Tests -------------

    def test_large_numbers(self):
        # Large numbers with only odd digits
        self.assertEqual(unique_digits([1357913579]), [1357913579])
        self.assertEqual(unique_digits([999999999]), [999999999])
        
    def test_sorting_order(self):
        self.assertEqual(unique_digits([97, 13, 755, 31, 1]), [1, 13, 31, 97, 755])
        self.assertEqual(unique_digits([99, 77, 55, 33, 11]), [11, 33, 55, 77, 99])
        
    def test_empty_list(self):
        self.assertEqual(unique_digits([]), [])

    def test_all_odd(self):
        self.assertEqual(unique_digits([135, 357, 579]), [135, 357, 579])

if __name__ == "__main__":
    unittest.main()
