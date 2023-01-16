# 463. Island Perimeter

# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        dirs = (-1, 0, 1, 0, -1)
        def dfs(r, c):
            if (not (0 <= r < ROWS) or
                not (0 <= c < COLS) or
                grid[r][c] == 0):
                return 1
            if (r, c) in visit:
                return 0
            visit.add((r, c))
            perimeter = dfs(r, c + 1)
            perimeter += dfs(r + 1, c)
            perimeter += dfs(r, c - 1)
            perimeter += dfs(r - 1, c)
            return perimeter
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)
        