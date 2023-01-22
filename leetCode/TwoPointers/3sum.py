# 15. 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums) - 1

            while(l<r):
                sum = nums[i] + nums[l] + nums[r]
                if(sum < 0):
                    l += 1
                elif(sum > 0):
                    r -= 1
                else:
                    result.append([nums[i], nums[l] , nums[r]])
                    l += 1
                    while(nums[l] == nums[l-1] and l < r):
                        l += 1

        return result