import unittest


def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    result = ''
    for char in string:
        if 'a' <= char <= 'z':
            result += char.upper()
        elif 'A' <= char <= 'Z':
            result += char.lower()
        else:
            result += char
    return result


class TestFlipCase(unittest.TestCase):
    def test_flip_case(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')
        self.assertEqual(flip_case('WORLD'), 'world')
        self.assertEqual(flip_case('1234'), '1234')
        self.assertEqual(flip_case('MiXeD'), 'mIxEd')
        self.assertEqual(flip_case(''), '')


if __name__ == '__main__':
    unittest.main()