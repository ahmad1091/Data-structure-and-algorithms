# 1691. Maximum Height by Stacking Cuboids 

# Given n cuboids where the dimensions of the ith cuboid is cuboids[i] = [widthi, lengthi, heighti] (0-indexed). Choose a subset of cuboids and place them on each other.

# You can place cuboid i on cuboid j if widthi <= widthj and lengthi <= lengthj and heighti <= heightj. You can rearrange any cuboid's dimensions by rotating it to put it on another cuboid.

# Return the maximum height of the stacked cuboids.

 

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        n = len(cuboids)

        for c in cuboids:
            c.sort()
        cuboids.sort()
        
        dp = [0] * n
        for i in range(n):
            dp[i] = cuboids[i][2]
            for j in range(i):
                if cuboids[j][0] <= cuboids[i][0] and cuboids[j][1] <= cuboids[i][1] and cuboids[j][2] <= cuboids[i][2]:
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])
        return max(dp)
