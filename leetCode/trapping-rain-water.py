# 42. Trapping Rain Water

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [None] * len(height)
        maxRight = [None] * len(height)

        mx = height[0]
        for i in range(len(height)):
            maxLeft[i] = mx
            mx = max(mx,height[i])

        mx = height[len(height)-1]
        for i in range(len(height)-1,-1,-1):
            maxRight[i] = mx
            mx = max(mx,height[i])

        qty = 0
        for i in range(len(height)):
            val = min(maxRight[i],maxLeft[i]) - height[i]
            if val >= 0:
                qty += val

        return qty