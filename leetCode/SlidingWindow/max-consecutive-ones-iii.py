# 1004. Max Consecutive Ones III

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, max = 0, 0

        for r in range(len(nums)):
            k -= (1 - nums[r])

            if k < 0:
                k += (1 - nums[r])
                l += 1

            res = max(res, r - l +1)
        
        return res