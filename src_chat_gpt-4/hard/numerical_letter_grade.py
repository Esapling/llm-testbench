def numerical_letter_grade(grades):
    result = []
    for g in grades:
        if g == 4.0:
            result.append('A+')
        elif g > 3.7:
            result.append('A')
        elif g > 3.3:
            result.append('A-')
        elif g > 3.0:
            result.append('B+')
        elif g > 2.7:
            result.append('B')
        elif g > 2.3:
            result.append('B-')
        elif g > 2.0:
            result.append('C+')
        elif g > 1.7:
            result.append('C')
        elif g > 1.3:
            result.append('C-')
        elif g > 1.0:
            result.append('D+')
        elif g > 0.7:
            result.append('D')
        elif g > 0.0:
            result.append('D-')
        else:
            result.append('E')
    return result

import unittest

class TestNumericalLetterGrade(unittest.TestCase):
    def test_example(self):
        self.assertEqual(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]), ['A+', 'B', 'C-', 'C', 'A-'])