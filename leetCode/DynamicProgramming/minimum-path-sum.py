# 64. Minimum Path Sum

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# sol 1:
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxInt =  2**31 - 1
        cache = {}
 
        def dfs(m, n):
            if (m, n) in cost: return cache[(m, n)]
            if (n < 0 or m < 0):
                return maxInt
            elif (m == 0 and n == 0):
                return grid[m][n]
            else:
                cost = grid[m][n] + min(dfs(m-1, n),dfs(m, n-1))
                cache[(m, n)] = cost
                return cost

        return dfs(ROWS - 1, COLS - 1)

# sol 2: dp solution O(m * n)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxInt =  2**31 - 1
        cache = {}
 
        def dfs(m, n):
            if (m, n) in cache: return cache[(m, n)]
            if (n < 0 or m < 0):
                return maxInt
            elif (m == 0 and n == 0):
                return grid[m][n]
            else:
                cost = grid[m][n] + min(dfs(m-1, n),dfs(m, n-1))
                cache[(m, n)] = cost
                return cost

        return dfs(ROWS - 1, COLS - 1)

# sol 3:
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[float('inf')] * (COLS + 1) for _ in range(ROWS + 1)]
        dp[ROWS - 1][COLS] = 0

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])
        return dp[0][0]