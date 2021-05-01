from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0

        r = len(grid)
        c = len(grid[0])
        cnt = 0

        for x in range(r):
            for y in range(c):
                if grid[x][y] == '1':
                    self.explore(grid, x, y)
                    cnt += 1

        return cnt

    def explore(self, grid, x, y):
        r = len(grid)
        c = len(grid[0])

        if not (x >= 0 and x < r and y >= 0 and y < c):
            return
        if grid[x][y] != '1':
            return
        grid[x][y] = '-1'
        self.explore(grid, x+1, y)
        self.explore(grid, x-1, y)
        self.explore(grid, x, y+1)
        self.explore(grid, x, y-1)

map = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
cnt = Solution().numIslands(map)
print(cnt)