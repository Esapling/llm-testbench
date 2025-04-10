import unittest


def exchange(s):
    """
    Given a string, return a version where the first and last characters have been exchanged.
    Don't treat numbers as a special case.
    exchange('abcd') → 'dbca'
    exchange('a') → 'a'
    exchange('xyz') → 'zyx'
    """
    if len(s) <= 1:
        return s
    else:
        return s[-1] + s[1:-1] + s[0]


class TestExchange(unittest.TestCase):
    def test_exchange(self):
        self.assertEqual(exchange('abcd'), 'dbca')
        self.assertEqual(exchange('a'), 'a')
        self.assertEqual(exchange('xyz'), 'zyx')
        self.assertEqual(exchange('1234'), '4231')
        self.assertEqual(exchange('ab'), 'ba')
        self.assertEqual(exchange(''), '')


if __name__ == '__main__':
    unittest.main()