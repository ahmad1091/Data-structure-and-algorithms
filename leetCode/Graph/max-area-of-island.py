# 695. Max Area of Island

# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

# sol 1: DFS
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = (1, 0, -1, 0, 1)
        self.maxArea = 0
        def dfs(r, c):
            grid[r][c] = 0
            self.count += 1
            for i, j in pairwise(dirs):
                x, y = r + i, c + j
                if(0 <= x < ROWS and
                   0 <= y < COLS and
                   grid[x][y] == 1):
                    dfs(x, y)
                    
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    self.count = 0
                    dfs(r, c)
                    self.maxArea = max(self.maxArea, self.count)

        return self.maxArea

# sol 2: bfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = (1, 0, -1, 0, 1)
        self.maxArea = 0
        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            while q:
                self.count += 1
                r, c = q.popleft()
                for i, j in pairwise(dirs):
                    x, y = r + i, c + j
                    if(0 <= x < ROWS and
                       0 <= y < COLS and
                       grid[x][y] == 1):
                        q.append((x, y))
                        grid[x][y] = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    self.count = 0
                    bfs(r, c)
                    self.maxArea = max(self.maxArea, self.count)

        return self.maxArea