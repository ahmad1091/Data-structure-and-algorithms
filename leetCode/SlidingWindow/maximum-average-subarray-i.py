# 643. Maximum Average Subarray I

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# Any answer with a calculation error less than 10-5 will be accepted.


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if (k > len(nums)): return -1
            
        sum =  nums[0]
        
        for i in range(1,k):
            sum += nums[i]
            
        max_sum = sum

        for i in range(k,len(nums)):
            sum = sum + nums[i] - nums[i-k]
            if sum > max_sum:
                max_sum = sum
        
    return max_sum / k