# 287. Find the Duplicate Number

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

class Solution:
    # Floyd's Cycle Detection method
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0

        while(True):
            fast = nums[nums[fast]]
            slow = nums[slow]
            if(slow == fast):
                break
        
        head = 0
        while(True):
            slow = nums[slow]
            head = nums[head]
            if(head == slow):
                break
        return slow