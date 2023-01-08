# Stack of Boxes: You have a stack of n boxes, with widths Wi ' heights hi ' and depths d i . The boxes
# cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly
# larger than the box above it in width, height, and depth. Implement a method to compute the
# height of the tallest possible stack. The height of a stack is the sum of the heights of each box.

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