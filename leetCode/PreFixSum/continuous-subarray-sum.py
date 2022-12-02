# 523. Continuous Subarray Sum

# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

class Solution:
    def checkSubarraySum(self, nums, k):
        reminder = {0:-1}
        total = 0
        for i,n in enumerate(nums):
            total += n
            r = total % k
            if r not in reminder:
                reminder[r] = i
            elif i - reminder[r] >1:
                return True

        return False
            
        


d = Solution()
print(d.checkSubarraySum([23,2,4,6,7],6))

