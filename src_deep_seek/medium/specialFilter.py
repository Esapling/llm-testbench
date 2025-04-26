import unittest

def specialFilter(nums):
    """
    Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    """
    count = 0
    for num in nums:
        if num > 10:
            s = str(abs(int(num)))
            first = int(s[0])
            last = int(s[-1])
            if first % 2 == 1 and last % 2 == 1:
                count += 1
    return count

class TestSpecialFilter(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
    
    def test_example2(self):
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)
    
    def test_all_valid(self):
        self.assertEqual(specialFilter([11, 13, 15, 17, 19, 31]), 6)
    
    def test_none_valid(self):
        self.assertEqual(specialFilter([10, 20, 30, 40, 22, 44]), 0)
    
    def test_mixed(self):
        self.assertEqual(specialFilter([19, 22, 33, 44, 55, 66, 77, 88, 99]), 5)

if __name__ == "__main__":
    unittest.main()