def numerical_letter_grade(grades):
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
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """
    grade_map = {
        (4.0, 4.0): 'A+',      # exactly 4.0
        (3.7, 4.0): 'A',       # > 3.7 and < 4.0
        (3.3, 3.7): 'A-',      # > 3.3 and <= 3.7
        (3.0, 3.3): 'B+',      # > 3.0 and <= 3.3
        (2.7, 3.0): 'B',       # > 2.7 and <= 3.0
        (2.3, 2.7): 'B-',      # > 2.3 and <= 2.7
        (2.0, 2.3): 'C+',      # > 2.0 and <= 2.3
        (1.7, 2.0): 'C',       # > 1.7 and <= 2.0
        (1.3, 1.7): 'C-',      # > 1.3 and <= 1.7
        (1.0, 1.3): 'D+',      # > 1.0 and <= 1.3
        (0.7, 1.0): 'D',       # > 0.7 and <= 1.0
        (0.0, 0.7): 'D-',      # > 0.0 and <= 0.7
        (0.0, 0.0): 'E'        # exactly 0.0
    }
    
    result = []
    
    for gpa in grades:
        letter_grade = ""
        
        # Handle the special cases of exactly 4.0 and 0.0
        if gpa == 4.0:
            letter_grade = 'A+'
        elif gpa == 0.0:
            letter_grade = 'E'
        else:
            # Find the appropriate grade range
            for (lower, upper), grade in grade_map.items():
                if lower < gpa <= upper:
                    letter_grade = grade
                    break
        
        result.append(letter_grade)
    
    return result


# Unit tests
import unittest

class TestNumericalLetterGrade(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]), ['A+', 'B', 'C-', 'C', 'A-'])
    
    def test_all_possible_grades(self):
        self.assertEqual(
            numerical_letter_grade([4.0, 3.8, 3.5, 3.2, 2.9, 2.5, 2.2, 1.9, 1.5, 1.2, 0.9, 0.5, 0.0]),
            ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E']
        )
    
    def test_boundary_values(self):
        self.assertEqual(
            numerical_letter_grade([3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7]),
            ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D']
        )
    
    def test_empty_list(self):
        self.assertEqual(numerical_letter_grade([]), [])
    
    def test_single_grade(self):
        self.assertEqual(numerical_letter_grade([3.9]), ['A'])
    
    def test_high_achievers(self):
        self.assertEqual(numerical_letter_grade([4.0, 4.0, 3.9, 3.8]), ['A+', 'A+', 'A', 'A'])
    
    def test_struggling_students(self):
        self.assertEqual(numerical_letter_grade([0.5, 0.3, 0.0]), ['D-', 'D-', 'E'])

if __name__ == "__main__":
    unittest.main()
