from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])

        visited = [[False for i in range(rows)] for i in range(cols)]
        self.fill(image, sr, sc, newColor, visited)
        return image

    def fill(self, image, x, y, newColor, visited):
        rows = len(image)
        cols = len(image[0])

        if x < 0 or x >= rows or y < 0 or y >= cols:
            return
        if visited[x][y]:
            return
        visited[x][y] = True
        image[x][y] = newColor

        self.fill(image, x-1, y, newColor, visited)
        self.fill(image, x+1, y, newColor, visited)
        self.fill(image, x, y+1, newColor, visited)
        self.fill(image, x, y-1, newColor, visited)

grid = [[1,1,1],[1,1,0],[1,0,1]]
new_grid = Solution().floodFill(grid, 1,1,2)
print(new_grid)

grid = [[False] * 3 for i in range(3)]
grid[1][1] = True
print(grid)