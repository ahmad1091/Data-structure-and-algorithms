# 200. Number of Islands

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# sol 1: dfs 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r,c):
            grid[r][c] = '0'
            for a, b in pairwise(dirs):
                x, y = a + r, b + c
                if (0 <= x < ROWS and
                    0 <= y < COLS and
                    grid[x][y] == '1'):
                    dfs(x, y)
        res = 0
        dirs = (1, 0, -1, 0, 1)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    res += 1
        return res

# sol 2: bfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def bfs(r,c):
            q = deque()
            grid[r][c] = '0'
            q.append((r, c))
            while q:
                r, c = q.popleft()
                for a, b in pairwise(dirs):
                    x, y = a + r, b + c
                    if (0 <= x < ROWS and
                        0 <= y < COLS and
                        grid[x][y] == '1'):
                        q.append((x, y))
                        grid[x][y] = '0'
        res = 0
        dirs = (1, 0, -1, 0, 1)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    bfs(r, c)
                    res += 1
        return res