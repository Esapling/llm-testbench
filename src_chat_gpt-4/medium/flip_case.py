"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase """
    return string.swapcase()

class Test(unittest.TestCase):
    def test_flip_case(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')
        self.assertEqual(flip_case('world'), 'WORLD')
        self.assertEqual(flip_case('123'), '123')
        self.assertEqual(flip_case('ABCdef'), 'abcDEF')

if __name__ == "__main__":
    unittest.main()
