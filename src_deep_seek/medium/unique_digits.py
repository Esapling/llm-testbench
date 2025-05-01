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

if __name__ == "__main__":
    unittest.main()
    