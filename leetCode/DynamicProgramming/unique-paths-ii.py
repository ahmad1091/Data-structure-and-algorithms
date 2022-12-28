# 63. Unique Paths II

# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The testcases are generated so that the answer will be less than or equal to 2 * 109.

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for c in range(n):
            if obstacleGrid[0][c] == 1: break
            dp[0][c] = 1

        for r in range(m):
            if obstacleGrid[r][0] == 1: break
            dp[r][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if  obstacleGrid[i][j] == 1: continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]