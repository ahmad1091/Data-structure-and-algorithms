# 724. Find Pivot Index

# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        prefixSum = 0
        
        for i in range(len(nums)):
            if(prefixSum == totalSum - nums[i]):
                return i
            prefixSum += nums[i];
            totalSum -= nums[i];
            
        return -1