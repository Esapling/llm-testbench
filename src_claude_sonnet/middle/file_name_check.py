def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    # Check if the file name contains exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # Split the file name into name and extension
    name, extension = file_name.split('.')
    
    # Check if name is empty or doesn't start with a letter
    if not name or not name[0].isalpha():
        return 'No'
    
    # Check if extension is valid
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # Count digits in the file name
    digit_count = sum(1 for char in file_name if char.isdigit())
    if digit_count > 3:
        return 'No'
    
    # If all conditions are met
    return 'Yes'

import unittest

class TestFileNameCheck(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(file_name_check("example.txt"), 'Yes')
        self.assertEqual(file_name_check("1example.dll"), 'No')
        
    def test_valid_names(self):
        self.assertEqual(file_name_check("file.txt"), 'Yes')
        self.assertEqual(file_name_check("program.exe"), 'Yes')
        self.assertEqual(file_name_check("library.dll"), 'Yes')
        self.assertEqual(file_name_check("file123.txt"), 'Yes')
        
    def test_invalid_extensions(self):
        self.assertEqual(file_name_check("file.jpg"), 'No')
        self.assertEqual(file_name_check("program.py"), 'No')
        self.assertEqual(file_name_check("test.pdf"), 'No')
        
    def test_too_many_digits(self):
        self.assertEqual(file_name_check("file1234.txt"), 'No')
        self.assertEqual(file_name_check("prog1234.exe"), 'No')
        
    def test_invalid_name_start(self):
        self.assertEqual(file_name_check("1file.txt"), 'No')
        self.assertEqual(file_name_check("_program.exe"), 'No')
        self.assertEqual(file_name_check("123.dll"), 'No')
        
    def test_multiple_dots(self):
        self.assertEqual(file_name_check("file.name.txt"), 'No')
        self.assertEqual(file_name_check("program..exe"), 'No')
        
    def test_empty_name(self):
        self.assertEqual(file_name_check(".txt"), 'No')

if __name__ == "__main__":
    unittest.main()
