from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    max_area = max(max_area, self.explore(grid, x, y))
        return max_area

    def explore(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return 0
        if grid[x][y] != 1:
            return 0
        grid[x][y] = -1
        return 1 + self.explore(grid, x+1, y) +\
               self.explore(grid, x-1, y) + \
               self.explore(grid, x, y+1) + \
               self.explore(grid, x, y-1)