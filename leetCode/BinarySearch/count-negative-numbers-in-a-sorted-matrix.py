# 1351. Count Negative Numbers in a Sorted Matrix

# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n, m = len(grid[0]), len(grid)
        x, y = 0, m - 1
        res = 0
        while x < m and y >= 0:
            if grid[y][x] < 0:
                res += n - x
                y -= 1

            else:
                x += 1

        return res