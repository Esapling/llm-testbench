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
        
    # ------------- Phase 2 Tests -------------
    
    def test_empty_string(self):
        self.assertEqual(flip_case(''), '')
        
    def test_numbers_and_symbols(self):
        self.assertEqual(flip_case('Hello123!'), 'hELLO123!')
        self.assertEqual(flip_case('!@#'), '!@#')

    def test_all_uppercase(self):
        self.assertEqual(flip_case('UPPERCASE'), 'uppercase')
    
    def test_all_lowercase(self):
        self.assertEqual(flip_case('lowercase'), 'LOWERCASE')
    
    def test_unicode_characters(self):
        self.assertEqual(flip_case('Hello, 世界!'), 'hELLO, 世界!')
        self.assertEqual(flip_case('¡Hola! ¿Cómo estás?'), '¡hOLA! ¿cÓMO ESTÁS?')


if __name__ == "__main__":
    unittest.main()
