"""
/* @Authors
* Student Names: Enes Fidan, Yunus Emre Bayraktar 
* Student IDs: 150200713, 150200020 
*/
"""
import unittest

def minPath(grid, k):
    """Find the lexicographically minimum path of length k."""
    def dfs(x, y, path):
        if len(path) == k:
            return path
        options = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                options.append(dfs(nx, ny, path + [grid[nx][ny]]))
        return min(options, key=lambda x: ''.join(map(str, x)))

    return dfs(0, 0, [grid[0][0]])

class Test(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(minPath([[1,2,3], [4,5,6], [7,8,9]], 3), [1, 2, 1])
    def test_single(self):
        self.assertEqual(minPath([[5,9,3], [4,1,6], [7,8,2]], 1), [1])
    def test_large(self):
        self.assertEqual(minPath([[1,2,3], [4,5,6], [7,8,9]], 5), [1, 2, 1, 2, 1])
    def test_complex(self):
        self.assertEqual(minPath([[5,9,3], [4,1,6], [7,8,2]], 4), [1, 6, 1, 6])

    #### Phase 2 Tests #### 
    #boundary case 2
    def test_min_grid_size(self):
        grid_min = [[1, 2], [3, 4]]
        self.assertEqual(minPath(grid_min, 1), [1])
        self.assertEqual(minPath(grid_min,2), [1,2])
        self.assertEqual(minPath(grid_min, 3), [1, 2, 1])

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
    def test_k_larger_than_grid(self):
        grid = [[1,2],[3,4]]
        self.assertEqual(minPath(grid, 4), [1,2,1,2])


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
