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
        self.assertEqual(specialFilter([12, 24, 35, 51]), 1)
        self.assertEqual(specialFilter([15, 25, 35]), 3)

if __name__ == "__main__":
    unittest.main()
