# 11. Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Solution 1: Brute Force
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxSpace = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                space = min(height[i],height[j]) * (j-i)
                maxSpace = space if space > maxSpace else maxSpace

        return maxSpace

# Solution 2:

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxSpace = 0
        while(l<r):
            space = min(height[r],height[l]) * (r-l)
            maxSpace = max(maxSpace,space)
            if height[l] <= height[r]:
                l += 1
            elif  height[l]>height[r]:
                r -= 1

        return maxSpace