"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest
import re

def file_name_check(file_name):
    """
    Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    """
    pattern = r'^[a-zA-Z][^.]*\.(txt|exe|dll)$'
    if not re.fullmatch(pattern, file_name):
        return 'No'
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'
    return 'Yes'

class TestFileNameCheck(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(file_name_check("example.txt"), 'Yes')
    
    def test_example2(self):
        self.assertEqual(file_name_check("1example.dll"), 'No')
    
    def test_valid(self):
        self.assertEqual(file_name_check("file1.exe"), 'Yes')
    
    def test_too_many_digits(self):
        self.assertEqual(file_name_check("file1234.txt"), 'No')
    
    def test_no_dot(self):
        self.assertEqual(file_name_check("filetxt"), 'No')
    
    def test_multiple_dots(self):
        self.assertEqual(file_name_check("file.txt.exe"), 'No')
    
    def test_invalid_extension(self):
        self.assertEqual(file_name_check("file.doc"), 'No')

if __name__ == "__main__":
    unittest.main()