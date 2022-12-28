# Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
# The robot can only move in two directions, right and down, but certain cells are "off limits" such that
# the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
# the bottom right.

class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
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

