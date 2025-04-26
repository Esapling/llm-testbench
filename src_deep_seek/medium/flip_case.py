import unittest

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase."""
    return string.swapcase()

class TestFlipCase(unittest.TestCase):
    def test_example(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')
    
    def test_mixed_case(self):
        self.assertEqual(flip_case('PyThOn'), 'pYtHoN')
    
    def test_all_upper(self):
        self.assertEqual(flip_case('WORLD'), 'world')
    
    def test_all_lower(self):
        self.assertEqual(flip_case('python'), 'PYTHON')
    
    def test_with_numbers(self):
        self.assertEqual(flip_case('Hello123'), 'hELLO123')

if __name__ == "__main__":
    unittest.main()