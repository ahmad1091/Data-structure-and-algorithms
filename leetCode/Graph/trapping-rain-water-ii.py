# 407. Trapping Rain Water II

# Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

 class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ROWS, COLS = len(heightMap), len(heightMap[0])
        pq = []

        for r in range(ROWS):
            for c in range(COLS):
                if r in {0, ROWS - 1} or c in {0, COLS - 1}:
                    heapq.heappush(pq, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1

        res = 0
        while pq:
            h, i, j = heapq.heappop(pq)
            for x, y in pairwise((1, 0, -1, 0, 1)):
                r, c = i + x, j + y
                if r < 0 or c < 0 or r >= ROWS or c >= COLS or heightMap[r][c] == -1:
                    continue
                res += max(0, h - heightMap[r][c])
                heapq.heappush(pq, (max(h, heightMap[r][c]), r, c))
                heightMap[r][c] = -1

        return res 
                
            
