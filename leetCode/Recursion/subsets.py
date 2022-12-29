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

# Solution #2:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allsubsets = []
        subset = []
        def dfs(i: int) -> List[List[int]]:
            if len(nums) <= i:
                allsubsets.append(subset.copy()) 
                return

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return allsubsets

            