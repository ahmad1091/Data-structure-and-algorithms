# 503. Next Greater Element II

# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number.
# If it doesn't exist, return -1 for this number.

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)

        for i in range(len(nums)):
            if i == stack[-1]:
                break
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            
        return res