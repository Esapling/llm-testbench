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

if __name__ == "__main__":
    unittest.main()