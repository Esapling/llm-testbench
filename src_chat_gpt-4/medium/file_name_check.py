"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest
import re

def file_name_check(file_name):
    """ Check if a file name is valid """
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    name, ext = file_name.split('.')
    if not name[0].isalpha():
        return 'No'
    if ext not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
class Test(unittest.TestCase):
    def test_file_name_check(self):
        self.assertEqual(file_name_check('example.txt'), 'Yes')
        self.assertEqual(file_name_check('1example.dll'), 'No')
        self.assertEqual(file_name_check('example1234.txt'), 'No')
        self.assertEqual(file_name_check('example.exe'), 'Yes')
        
    # -------------- Phase 2 Tests --------------
    
    def test_invalid_extension(self):
        self.assertEqual(file_name_check('file.doc'), 'No')
        self.assertEqual(file_name_check('file.dll'), 'Yes')
        self.assertEqual(file_name_check('file.txt'), 'Yes')
    
    def test_multiple_dots(self):
        self.assertEqual(file_name_check('file.txt.exe'), 'No')
        self.assertEqual(file_name_check('file.txt'), 'Yes')
    
    def test_no_dot(self):
        self.assertEqual(file_name_check('filetxt'), 'No')
        self.assertEqual(file_name_check('file'), 'No')
        
    def test_empty_name(self):
        self.assertEqual(file_name_check('.txt'), 'No')
        self.assertEqual(file_name_check('file.'), 'No')
        self.assertEqual(file_name_check('.'), 'No')



        
        
        
        
    

if __name__ == "__main__":
    unittest.main()
