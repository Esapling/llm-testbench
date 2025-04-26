
import unittest

def exchange(lst1, lst2):
    has_even = any(x % 2 == 0 for x in lst2)
    if not has_even:
        return "NO"
    return "YES"

class TestExchange(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

    def test_all_even_in_lst2(self):
        self.assertEqual(exchange([1,3,5], [2,4,6]), "YES")

if __name__ == "__main__":
    unittest.main()
