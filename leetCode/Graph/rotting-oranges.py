# 994. Rotting Oranges

# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        dirs = (1, 0, -1, 0, 1)
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for i, j in pairwise(dirs):
                    x, y = r + i, c + j
                    if(not(0 <= x < ROWS) or
                       not(0 <= y < COLS) or
                       grid[x][y] != 1):
                       continue
                    grid[x][y] = 2
                    fresh -= 1
                    q.append((x, y))
            time += 1
        return time if fresh == 0 else -1
                

