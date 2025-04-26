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

if __name__ == "__main__":
    unittest.main()
