from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        for x in range(rows):
            y = 0
            if grid[x][y] == 1:
                self.explore(grid, x, y)
            y = cols-1
            if grid[x][y] == 1:
                self.explore(grid, x, y)

        for y in range(cols):
            x = 0
            if grid[x][y] == 1:
                self.explore(grid, x, y)
            x = rows-1
            if grid[x][y] == 1:
                self.explore(grid, x, y)

        return sum(row.count(1) for row in grid)

    def explore(self, grid, x, y):
        rows = len(grid)
        cols = len(grid[0])

        if x < 0 or x >= rows or y < 0 or y >= cols:
            return
        if grid[x][y] != 1:
            return
        grid[x][y] = -1

        self.explore(grid, x+1, y)
        self.explore(grid, x-1, y)
        self.explore(grid, x, y+1)
        self.explore(grid, x, y-1)

grid = [[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]]
n = Solution().numEnclaves(grid)
print(n)