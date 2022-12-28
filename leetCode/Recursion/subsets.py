# 78. Subsets

# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Solution #1: Recursion
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subsets(nums: List[int], i: int) -> List[List[int]]:
            allsubsets = []

            if len(nums) == i:
                allsubsets.append([]) 
            else:
                allsubsets = subsets(nums, i + 1)
                item = nums[i]
                moresubsets = []

                for subset in allsubsets:
                    newsubset = []
                    newsubset += subset
                    newsubset.append(item)
                    moresubsets.append(newsubset)

                allsubsets += moresubsets

            return allsubsets

        return subsets(nums, 0)

# Solution #2: Combinatorics
class Solution:
    def convertItToSet(self, x: int, arr: list[int]):
        subset = []
        idx = 0

        for k in range(x - 1, 0, -1):
            if (k & 1) == 1:
                subset.append(arr[idx]) 
            idx += 1
            
        return subset
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allsubsets = []
        max = 1 << len(nums)

        for k in range(max):
            subset = self.convertItToSet(k, nums)
            allsubsets.append(subset)

        return allsubsets