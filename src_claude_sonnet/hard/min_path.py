"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
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
    """
    n = len(grid)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
    best_path = None
    
    # Try starting from each cell
    for i in range(n):
        for j in range(n):
            # DFS from current cell
            current_path = [grid[i][j]]
            
            def dfs(row, col, path_length):
                nonlocal best_path
                
                # If we've reached path length k, check if this path is better
                if path_length == k:
                    if best_path is None or current_path < best_path:
                        best_path = current_path.copy()
                    return
                
                # If we already have a best path and current path is worse, prune
                if best_path is not None and current_path > best_path[:path_length]:
                    return
                
                # Try each direction
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    
                    # Check if the new position is valid
                    if 0 <= new_row < n and 0 <= new_col < n:
                        # Add this cell to our path
                        current_path.append(grid[new_row][new_col])
                        
                        # Continue DFS
                        dfs(new_row, new_col, path_length + 1)
                        
                        # Backtrack
                        current_path.pop()
            
            # Start DFS from this cell
            dfs(i, j, 1)
    
    return best_path
import unittest
from min_path import minPath  # Assuming the function is saved in min_path.py

class TestMinPath(unittest.TestCase):
    
    def test_example_1(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 3
        expected = [1, 2, 1]
        self.assertEqual(minPath(grid, k), expected)
    
    def test_example_2(self):
        grid = [[5, 9, 3], [4, 1, 6], [7, 8, 2]]
        k = 1
        expected = [1]
        self.assertEqual(minPath(grid, k), expected)
    
    def test_length_2(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 2
        expected = [1, 2]
        self.assertEqual(minPath(grid, k), expected)
    
    def test_small_grid(self):
        grid = [[1, 3], [2, 4]]
        k = 4
        expected = [1, 2, 1, 2]
        self.assertEqual(minPath(grid, k), expected)
    
    def test_revisit_cells(self):
        grid = [[2, 1], [3, 4]]
        k = 5
        expected = [1, 2, 1, 2, 1]
        self.assertEqual(minPath(grid, k), expected)
    
    def test_larger_grid(self):
        grid = [
            [1, 2, 3, 4],
            [8, 7, 6, 5],
            [9, 10, 11, 12],
            [16, 15, 14, 13]
        ]
        k = 3
        expected = [1, 2, 1]
        self.assertEqual(minPath(grid, k), expected)

if __name__ == '__main__':
    unittest.main()
