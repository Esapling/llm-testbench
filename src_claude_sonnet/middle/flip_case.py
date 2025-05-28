"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
def flip_case(string: str) -> str:
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(char.lower() if char.isupper() else char.upper() for char in string)

import unittest

class TestFlipCase(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')
        
    def test_all_uppercase(self):
        self.assertEqual(flip_case('WORLD'), 'world')
        
    def test_all_lowercase(self):
        self.assertEqual(flip_case('python'), 'PYTHON')
        
    def test_mixed_case(self):
        self.assertEqual(flip_case('PyThOn'), 'pYtHoN')
        
    def test_with_numbers_symbols(self):
        self.assertEqual(flip_case('Hello123!'), 'hELLO123!')
        
    def test_empty_string(self):
        self.assertEqual(flip_case(''), '')

    # ------------- Phase 2 Tests -------------
    
    def test_unicode_characters(self):
        self.assertEqual(flip_case('Hello, 世界!'), 'hELLO, 世界!')
        self.assertEqual(flip_case('¡Hola! ¿Cómo estás?'), '¡hOLA! ¿cÓMO ESTÁS?')



if __name__ == "__main__":
    unittest.main()
