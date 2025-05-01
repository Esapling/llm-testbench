"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def numerical_letter_grade(grades):
    """ Convert numerical grades to letter grades """
    letter_grades = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grades.append('A+')
        elif gpa > 3.7:
            letter_grades.append('A')
        elif gpa > 3.3:
            letter_grades.append('A-')
        elif gpa > 3.0:
            letter_grades.append('B+')
        elif gpa > 2.7:
            letter_grades.append('B')
        elif gpa > 2.3:
            letter_grades.append('B-')
        elif gpa > 2.0:
            letter_grades.append('C+')
        elif gpa > 1.7:
            letter_grades.append('C')
        elif gpa > 1.3:
            letter_grades.append('C-')
        elif gpa > 1.0:
            letter_grades.append('D+')
        elif gpa > 0.7:
            letter_grades.append('D')
        elif gpa > 0.0:
            letter_grades.append('D-')
        else:
            letter_grades.append('E')
    return letter_grades

class TestNumericalLetterGrade(unittest.TestCase):
    def test_example(self):
        self.assertEqual(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]), 
                         ['A+', 'B', 'C-', 'C', 'A-'])
    
    def test_all_grades(self):
        test_grades = [4.0, 3.8, 3.5, 3.2, 3.0, 2.8, 2.5, 2.2, 2.0, 
                      1.8, 1.5, 1.2, 1.0, 0.8, 0.5, 0.0]
        expected = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 
                    'D+', 'D', 'D-', 'E', 'E', 'E', 'E']
        self.assertEqual(numerical_letter_grade(test_grades), expected)
    
    def test_empty(self):
        self.assertEqual(numerical_letter_grade([]), [])

if __name__ == "__main__":
    unittest.main()