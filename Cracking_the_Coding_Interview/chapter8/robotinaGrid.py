# Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
# The robot can only move in two directions, right and down, but certain cells are "off limits" such that
# the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
# the bottom right.

def pathWithObstacles(obstacleGrid: list[list]):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    res = []

    def dfs(i:int, j:int) -> bool:
        if i == m | j == n | obstacleGrid[i][j] == 1:
            return False

        res.append([i, j])
        obstacleGrid[i][j] = 1
        
        if (i + 1 == m & j + 1 == n) | dfs(i + 1, j) | dfs(i, j + 1):
            return True

        res.pop()
        return  False

    if dfs(0,0):
        return True
    
    return []
