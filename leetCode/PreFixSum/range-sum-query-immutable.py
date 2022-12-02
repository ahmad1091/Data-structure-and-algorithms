# 303. Range Sum Query - Immutable

# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

class NumArray:

    def __init__(self, nums: List[int]):
        sum = 0
        arr = [0] * len(nums)
        for i,n in enumerate(nums):
            sum += n
            arr[i] = sum
        self.nums = arr

    def sumRange(self, left: int, right: int) -> int:
        
        if left - 1 < 0:
            return self.nums[right] 
        else:
            return self.nums[right] - self.nums[left-1]
            
            


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)