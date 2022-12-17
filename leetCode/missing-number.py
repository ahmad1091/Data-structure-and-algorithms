# 268. Missing Number

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# sol 1:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums) + 1):
            if (i not in nums  or i != nums[i]):
                return i

# sol 2:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        return res
