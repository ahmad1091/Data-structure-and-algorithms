# 1920. Build Array from Permutation

# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = [nums[0]] * len(nums)
        for i, n in enumerate(nums):
            res[i] = nums[n]
        
        return res

# sol 2:
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[num] for num in nums]