# 90. Subsets II

# Given an integer array nums that may contain duplicates, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subSets = []
        nums.sort()

        def backTrack(i, subset):
            if i == len(nums):
                subSets.append(subset[:])
                return

            subset.append(nums[i])
            backTrack(i + 1, subset)
            subset.pop()

            while(i + 1 < len(nums) and nums[i] == nums[i + 1]):
                 i += 1
            
            backTrack(i + 1, subset)

        backTrack(0, [])
        return subSets