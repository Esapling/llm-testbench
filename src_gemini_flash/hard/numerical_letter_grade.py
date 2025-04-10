import unittest


def numerical_letter_grade(marks):
    """
    Given a list of numerical marks, return the corresponding list of letter grades.
    """
    grades = []
    for mark in marks:
        if 90 <= mark <= 100:
            grades.append('A')
        elif 80 <= mark < 90:
            grades.append('B')
        elif 70 <= mark < 80:
            grades.append('C')
        elif 60 <= mark < 70:
            grades.append('D')
        else:
            grades.append('F')
    return grades


class TestNumericalLetterGrade(unittest.TestCase):
    def test_numerical_letter_grade(self):
        self.assertEqual(numerical_letter_grade([90, 80, 70, 60, 50]), ['A', 'B', 'C', 'D', 'F'])
        self.assertEqual(numerical_letter_grade([100, 85, 75, 65, 55]), ['A', 'B', 'C', 'D', 'F'])
        self.assertEqual(numerical_letter_grade([95, 89, 79, 69, 59]), ['A', 'B', 'C', 'D', 'F'])
        self.assertEqual(numerical_letter_grade([0, 100]), ['F', 'A'])
        self.assertEqual(numerical_letter_grade([]), [])
        self.assertEqual(numerical_letter_grade([70, 71, 79]), ['C', 'C', 'C'])


if __name__ == '__main__':
    unittest.main()