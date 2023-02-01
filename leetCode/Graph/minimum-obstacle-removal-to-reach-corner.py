# 2290. Minimum Obstacle Removal to Reach Corner

# You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

# 0 represents an empty cell,
# 1 represents an obstacle that may be removed.
# You can move up, down, left, or right from and to an empty cell.

# Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque([(0, 0, 0)])

        while q:
            i, j, k = q.popleft()
            if i == ROWS - 1 and j == COLS -1:
                return k
            if grid[i][j] == -1 : 
                continue

            grid[i][j] = -1

            for x, y in pairwise((1, 0, -1, 0, 1)):
                r, c = i + x, j + y
                if 0 <= r < ROWS and 0 <= c < COLS:
                    if grid[r][c] == 0:
                        q.appendleft((r, c, k))
                    else:
                        q.append((r, c, k + 1))