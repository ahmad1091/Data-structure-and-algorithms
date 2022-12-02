# 1480. Running Sum of 1d Array

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = [0]* len(nums)
        arr[0] = nums [0]
        for i in range(1,len(nums)):
            arr [i] = nums[i] + arr[i-1]         
            
        return arr