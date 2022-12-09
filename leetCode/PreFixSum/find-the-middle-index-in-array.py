# 1991. Find the Middle Index in Array

# Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).

# A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

# If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.

# Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.


# solution 1:
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sum = [0]*n
        sum[0] = nums[0]
        for i in range(1,n):
            sum[i] = nums[i] + sum[i-1]

        for i in range(n):
            if sum [i] - nums[i] == sum[n-1] - sum[i]:
                return i
        return -1

