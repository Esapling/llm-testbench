def minPath(grid, k):
    from heapq import heappush, heappop
    n = len(grid)
    heap = []
    for i in range(n):
        for j in range(n):
            heappush(heap, ([grid[i][j]], i, j))
    for _ in range(k-1):
        new_heap = []
        while heap:
            path, x, y = heappop(heap)
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<n:
                    heappush(new_heap, (path+[grid[nx][ny]], nx, ny))
        heap = new_heap
    return heappop(heap)[0]

import unittest

class TestMinPath(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(minPath([[1,2,3],[4,5,6],[7,8,9]], 3), [1,2,1])
    def test_case2(self):
        self.assertEqual(minPath([[5,9,3],[4,1,6],[7,8,2]], 1), [1])