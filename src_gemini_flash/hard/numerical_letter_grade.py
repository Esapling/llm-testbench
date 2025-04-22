import unittest
from typing import List

def numerical_letter_grade(grades: List[float]) -> List[str]:
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A
            > 3.3                A-
            > 3.0                B+
            > 2.7                B
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+
            > 0.7                D
            > 0.0                D-
              0.0                E


    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B+', 'C', 'C+', 'A-']
    """
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
        else: # gpa must be 0.0 or less, but table only specifies 0.0
            letter_grades.append('E')
    return letter_grades

class TestNumericalLetterGrade(unittest.TestCase):

    def test_example_case(self):
        """Test the example case from the docstring."""
        # Corrected expected output based on the provided grading table
        self.assertEqual(numerical_letter_grade([4.0, 3.0, 1.7, 2.0, 3.5]), ['A+', 'B+', 'C', 'C+', 'A-'])

    def test_boundary_cases(self):
        """Test values at or near the boundaries of the grade ranges."""
        self.assertEqual(numerical_letter_grade([3.7, 3.75, 3.3, 3.35, 3.0, 3.05, 0.0, 0.05]),
                         ['D', 'A', 'D+', 'A-', 'D+', 'B+', 'E', 'D-']) # Corrected based on > thresholds

    def test_all_grade_categories(self):
        """Test inputs that should result in each possible letter grade."""
        self.assertEqual(numerical_letter_grade([4.0, 3.8, 3.5, 3.1, 2.8, 2.5, 2.1, 1.8, 1.5, 1.1, 0.8, 0.1, 0.0]),
                         ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E'])

    def test_empty_list(self):
        """Test with an empty input list."""
        self.assertEqual(numerical_letter_grade([]), [])

    def test_grades_on_thresholds(self):
        """Test grades that are exactly on the '>' thresholds."""
        self.assertEqual(numerical_letter_grade([3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]),
                         ['D', 'D+', 'D+', 'C', 'C-', 'C+', 'C', 'C-', 'D+', 'D', 'E']) # Corrected expected based on >

# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)