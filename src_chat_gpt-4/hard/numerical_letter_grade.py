import unittest

def numerical_letter_grade(grades):
    """Convert GPA values to letter grades."""
    grades_map = [
        (4.0, 'A+'),
        (3.7, 'A'),
        (3.3, 'A-'),
        (3.0, 'B+'),
        (2.7, 'B'),
        (2.3, 'B-'),
        (2.0, 'C+'),
        (1.7, 'C'),
        (1.3, 'C-'),
        (1.0, 'D+'),
        (0.7, 'D'),
        (0.0, 'D-'),
        (-0.1, 'E')
    ]
    result = []
    for gpa in grades:
        for cutoff, grade in grades_map:
            if gpa >= cutoff:
                result.append(grade)
                break
    return result

class Test(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]), ['A+', 'B', 'C-', 'C', 'A-'])
    def test_edge(self):
        self.assertEqual(numerical_letter_grade([0.0, 2.0, 3.7, 4.0]), ['E', 'C+', 'A', 'A+'])
    def test_mixed(self):
        self.assertEqual(numerical_letter_grade([3.1, 3.8, 2.5]), ['B+', 'A', 'B'])
    def test_single(self):
        self.assertEqual(numerical_letter_grade([1.0]), ['D+'])

if __name__ == "__main__":
    unittest.main()
