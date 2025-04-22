import heapq
import unittest

def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k,
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    Please note that a path of length k means visiting exactly k cells (not
    necessarily distinct).
    You CANNOT go off the grid.
    A path A (of length k) is considered less than a path B (of length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B, in other words, there exist an integer index i (1 <= i <= k)
    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.

    Examples:

        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]
    """
    n = len(grid)
    if n == 0 or k == 0:
        return []

    # Priority queue to store paths (value_list, row, col)
    # The priority queue will order elements based on the first element of the tuple, which is the path's value list.
    pq = []

    # Initialize PQ with all possible starting positions (paths of length 1)
    for r in range(n):
        for c in range(n):
            heapq.heappush(pq, ([grid[r][c]], r, c))

    # Directions for moving to neighbors (down, up, right, left)
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while pq:
        current_path_values, row, col = heapq.heappop(pq)

        # If the path length is k, we found the lexicographically smallest path
        if len(current_path_values) == k:
            return current_path_values

        # If path length is less than k, explore neighbors
        if len(current_path_values) < k:
            for i in range(4):
                new_row = row + dr[i]
                new_col = col + dc[i]

                # Check if the new position is within the grid bounds
                if 0 <= new_row < n and 0 <= new_col < n:
                    new_path_values = current_path_values + [grid[new_row][new_col]]
                    # Push the new path to the priority queue.
                    # The tuple's first element (the list) is used for priority.
                    heapq.heappush(pq, (new_path_values, new_row, new_col))

    return [] # Should not reach here based on problem constraints (N>=2, k>=1 and answer is unique)


class TestMinPath(unittest.TestCase):

    def test_example_1(self):
        """Test the first example case."""
        grid = [ [1,2,3], [4,5,6], [7,8,9]]
        k = 3
        self.assertEqual(minPath(grid, k), [1, 2, 1])

    def test_example_2(self):
        """Test the second example case (k=1)."""
        grid = [ [5,9,3], [4,1,6], [7,8,2]]
        k = 1
        self.assertEqual(minPath(grid, k), [1])

    def test_2x2_grid_k2(self):
        """Test a 2x2 grid with k=2."""
        grid = [ [4, 2], [3, 1] ]
        k = 2
        # The minimum value is 1. Neighbors are 2 and 3. [1, 2] is lexicographically smaller than [1, 3].
        self.assertEqual(minPath(grid, k), [1, 2])

    def test_2x2_grid_k3(self):
        """Test a 2x2 grid with k=3."""
        grid = [ [4, 2], [3, 1] ]
        k = 3
        # Paths of length 2 starting from 1: [1,2] (move to 2), [1,3] (move to 3). [1,2] is smaller.
        # From [1,2], neighbors of 2 are 4 and 1. Paths of length 3: [1,2,4], [1,2,1]. [1,2,1] is smaller.
        # From [1,3], neighbors of 3 are 4 and 1. Paths of length 3: [1,3,4], [1,3,1]. [1,3,1] is smaller.
        # Comparing the best paths starting with 1: [1,2,1] and [1,3,1]. [1,2,1] is smaller.
        # Check paths starting with other numbers:
        # From 2: [2,4], [2,1]. From [2,1], neighbors of 1 are 3 and 2. Paths [2,1,3], [2,1,2]. [2,1,2] is smaller.
        # Comparing [1,2,1] and [2,1,2], [1,2,1] is smaller.
        self.assertEqual(minPath(grid, k), [1, 2, 1])

    def test_3x3_grid_k2_different_values(self):
        """Test a 3x3 grid with different values and k=2."""
        grid = [ [9, 8, 7], [6, 5, 4], [3, 2, 1] ]
        k = 2
        # The minimum value is 1 at (2, 2). Its neighbors are 4 (at (1, 2)) and 2 (at (2, 1)).
        # Paths of length 2 starting with 1 are [1, 4] and [1, 2].
        # Lexicographically, [1, 2] is smaller.
        self.assertEqual(minPath(grid, k), [1, 2])


# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)