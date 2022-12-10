# 209. Minimum Size Subarray Sum

# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, sumo, length = 0, 0, float('inf')

        for r in range(len(nums)):
            sumo += nums[r]
            while sumo >= target:
                length = min(length, r - l + 1)
                sumo -= nums[l]
                l += 1
            
        return length if length < float('inf') else 0