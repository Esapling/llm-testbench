"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def minPath(grid, k):
    """ Find the minimum path of length k in the grid """
    n = len(grid)
    if n == 0:
        return []
    
    # Start with the smallest value in the grid
    min_val = min(min(row) for row in grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == min_val:
                start = (i, j)
                break
    
    path = [min_val]
    current = start
    for _ in range(k-1):
        i, j = current
        neighbors = []
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n:
                neighbors.append((ni, nj))
        
        # Find the neighbor with smallest value
        next_pos = min(neighbors, key=lambda pos: grid[pos[0]][pos[1]])
        path.append(grid[next_pos[0]][next_pos[1]])
        current = next_pos
    
    return path

class TestMinPath(unittest.TestCase):
    def test_example1(self):
        grid = [[1,2,3], [4,5,6], [7,8,9]]
        self.assertEqual(minPath(grid, 3), [1, 2, 1])
    
    def test_example2(self):
        grid = [[5,9,3], [4,1,6], [7,8,2]]
        self.assertEqual(minPath(grid, 1), [1])
    
    def test_single_cell(self):
        grid = [[1]]
        self.assertEqual(minPath(grid, 1), [1])
    
    def test_k_larger_than_grid(self):
        grid = [[1,2],[3,4]]
        self.assertEqual(minPath(grid, 4), [1,2,1,2])


    def test_min_value_at_diff_positions(self):
        #1 at top left 
        grid1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(minPath(grid1, 1), [1])

        # 1 at bottom right 
        grid2 = [[9, 2, 3], [4, 5, 6], [7, 8, 1]]
        self.assertEqual(minPath(grid2, 1), [1])

        # 1 at center
        grid3 = [[9, 8, 7], [6, 1, 5], [4, 3, 2]]
        self.assertEqual(minPath(grid3, 1), [1])
        
    def test_neigbor_selection(self):
        grid = [[3, 2, 9], 
            [4, 1, 5], 
            [8, 6, 7]]
        self.assertEqual(minPath(grid, 4), [1, 2, 1, 2])

    def test_large_grids(self):
        grid_large = [[1, 2, 3, 4, 5], 
                      [6, 7, 8, 9, 10], 
                      [11, 12, 13, 14, 15], 
                      [16, 17, 18, 19, 20], 
                      [21, 22, 23, 24, 25]]
        self.assertEqual(minPath(grid_large, 6), [1, 2, 1, 2, 1, 2])

    def test_lexiographical_order(self):
        grid = [[4, 3, 1], [2, 5, 6], [7, 8, 9]]

        # Multiple paths possible, should return lexicographically smallest
        for k in range(1, 6):
            path = minPath(grid, k)
            self.assertEqual(path[0], 1)  # start with minimum
            
            # path length must be k
            self.assertEqual(len(path), k)
            
            # values must be valid
            for val in path:
                self.assertTrue(1 <= val <= 9)
    
if __name__ == "__main__":
    unittest.main()