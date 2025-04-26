def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    result = []
    
    for num in x:
        # Check if all digits are odd
        if all(int(digit) % 2 == 1 for digit in str(num)):
            result.append(num)
    
    # Sort in increasing order
    return sorted(result)

import unittest

class TestUniqueDigits(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])
        
    def test_empty_list(self):
        self.assertEqual(unique_digits([]), [])
        
    def test_no_matches(self):
        self.assertEqual(unique_digits([2, 4, 6, 8, 10, 20]), [])
        
    def test_all_matches(self):
        self.assertEqual(unique_digits([1, 3, 5, 7, 9, 35, 79]), [1, 3, 5, 7, 9, 35, 79])
        
    def test_mixed_numbers(self):
        self.assertEqual(unique_digits([11, 13, 15, 20, 33, 42, 55]), [11, 13, 15, 33, 55])
        
    def test_large_numbers(self):
        self.assertEqual(unique_digits([11111, 22222, 33333, 55555]), [11111, 33333, 55555])

if __name__ == "__main__":
    unittest.main()
