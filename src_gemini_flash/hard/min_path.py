import unittest
import math

#this code could not be completed at first place, but in the secodn prompt
def minPath(matrix):
    """
    Given a 2D matrix, find the minimum path sum from the top-left cell to the bottom-right cell.
    You can only move either down or right at any point in time.
    """
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]

    dp[0][0] = matrix[0][0]

    # Initialize first row
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]

    # Initialize first column
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]

    # Calculate minimum path sum for the rest of the cells
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]

    return dp[rows - 1][cols - 1]


class TestMinPath(unittest.TestCase):
    def test_minPath(self):
        self.assertEqual(minPath([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)
        self.assertEqual(minPath([[1, 2], [3, 4]]), 8)
        self.assertEqual(minPath([[1]]), 1)
        self.assertEqual(minPath([[0]]), 0)
        self.assertEqual(minPath([[0, 0], [0, 0]]), 0)
        self.assertEqual(minPath([[2, 2], [2, 2]]), 8)
        self.assertEqual(minPath([[1, 1, 1], [2, 2, 2]]), 5)
        self.assertEqual(minPath([[1, 2, 3], [4, 5, 6]]), 12)
        self.assertEqual(minPath([]), 0)
        self.assertEqual(minPath([[]]), 0)


if __name__ == '__main__':
    unittest.main()