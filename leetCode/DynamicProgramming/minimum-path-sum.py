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

# sol 2: dp solution
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