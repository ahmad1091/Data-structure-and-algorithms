# 42. Trapping Rain Water

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# sol 1: Time: O(n) Space: O(n)
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

# Sol 2: Time: O(n) Space: O(1) Two Pointers

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        qty = 0
        
        while(l < r):
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                qty += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                qty += rightMax - height[r]

        return qty
