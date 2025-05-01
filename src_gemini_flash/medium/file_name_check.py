"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def file_name_check(file_name: str) -> str:
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
    file_name_check(""example.txt"") # => 'Yes'
    file_name_check(""1example.dll"") # => 'No' (the name should start with a latin alphapet letter)
    """
    # Condition 2: Exactly one dot '.'
    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    before_dot = parts[0]
    after_dot = parts[1]

    # Condition 3: Substring before the dot
    if not before_dot or not before_dot[0].isalpha():
        return 'No'

    # Condition 4: Substring after the dot (extension)
    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'

    # Condition 1: Not more than three digits
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'

    # If all conditions are met
    return 'Yes'

class TestFileNameCheck(unittest.TestCase):

    def test_valid_cases(self):
        """Test valid file names, including example 1 and max allowed digits."""
        self.assertEqual(file_name_check("example.txt"), 'Yes')
        self.assertEqual(file_name_check("name123.dll"), 'Yes')
        self.assertEqual(file_name_check("UPPER.exe"), 'Yes')
        self.assertEqual(file_name_check("a.txt"), 'Yes')
        self.assertEqual(file_name_check("file_name.txt"), 'Yes')


    def test_invalid_start_letter(self):
        """Test cases where the name before the dot does not start with a letter."""
        self.assertEqual(file_name_check("1example.dll"), 'No') # Example 2
        self.assertEqual(file_name_check("_file.txt"), 'No')
        self.assertEqual(file_name_check(".txt"), 'No') # Empty before dot


    def test_invalid_number_of_dots(self):
        """Test cases with more or less than one dot."""
        self.assertEqual(file_name_check("file.name.txt"), 'No')
        self.assertEqual(file_name_check("filename"), 'No')
        self.assertEqual(file_name_check("file.name."), 'No') # Dot at the end


    def test_invalid_extension(self):
        """Test cases with extensions not in the allowed list."""
        self.assertEqual(file_name_check("archive.zip"), 'No')
        self.assertEqual(file_name_check("document.pdf"), 'No')
        self.assertEqual(file_name_check("image.png"), 'No')


    def test_invalid_digit_count(self):
        """Test cases with more than three digits."""
        self.assertEqual(file_name_check("file1234.txt"), 'No')
        self.assertEqual(file_name_check("1234_name.exe"), 'No')
        self.assertEqual(file_name_check("a1b2c3d4.dll"), 'No')


# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)