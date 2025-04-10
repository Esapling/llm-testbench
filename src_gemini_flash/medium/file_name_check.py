import unittest
import re


def file_name_check(file_name):
    """
    Given a file name, return True if it is valid, False otherwise.
    A valid file name contains only letters, numbers, and underscores.
    It must have a dot and an extension of 3 characters.
    """
    pattern = r'^[a-zA-Z0-9_]+\.[a-zA-Z0-9]{3}$'
    return bool(re.match(pattern, file_name))


class TestFileNameCheck(unittest.TestCase):
    def test_file_name_check(self):
        self.assertEqual(file_name_check("hello.txt"), True)
        self.assertEqual(file_name_check("hello_world.txt"), True)
        self.assertEqual(file_name_check("123.txt"), True)
        self.assertEqual(file_name_check("hello.123"), True)
        self.assertEqual(file_name_check("hello.te"), False)
        self.assertEqual(file_name_check("hello.tex"), True)
        self.assertEqual(file_name_check("hello.text"), False)
        self.assertEqual(file_name_check("hello.txt1"), False)
        self.assertEqual(file_name_check("hello.tx"), False)
        self.assertEqual(file_name_check("hello world.txt"), False)
        self.assertEqual(file_name_check("hello.txt.txt"), False)
        self.assertEqual(file_name_check(""), False)


if __name__ == '__main__':
    unittest.main()