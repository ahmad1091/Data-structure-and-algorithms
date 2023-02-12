# 416. Partition Equal Subset Sum

# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

# sol :
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: return False
        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            clone = dp.copy()

            for elm in dp:
                clone.add(elm + nums[i])
            dp = clone

        return True if target in dp else False 