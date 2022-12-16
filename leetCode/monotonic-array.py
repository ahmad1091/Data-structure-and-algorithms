# 896. Monotonic Array

# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        flag = True
        for i in range(1,len(nums)):
            if not flag:
                break
            flag = flag and  nums[i] - nums[i-1] >= 0

        if flag: return True
        
        flag = True
        for i in range(1,len(nums)):
            if not flag:
                break
            flag = flag and  nums[i] - nums[i-1] <= 0

        return flag
                