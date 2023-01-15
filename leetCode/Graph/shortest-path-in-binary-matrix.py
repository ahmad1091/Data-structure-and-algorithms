# 1091. Shortest Path in Binary Matrix

# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:return -1
        q = deque([(0, 0)])
        grid[0][0] = 1
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        n = len(grid)
        des = 0
        while q:
            des += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r, c) == (n - 1, n - 1):
                    return des
                for i, j in dirs:
                    nextRow = r + i
                    nextCol = c + j
                    if 0 <= nextRow < n and 0 <= nextCol < n  and grid[nextRow][nextCol] == 0:
                        q.append((nextRow,nextCol))
                        grid[nextRow][nextCol] = 1
        return -1
                