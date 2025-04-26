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

if __name__ == "__main__":
    unittest.main()
