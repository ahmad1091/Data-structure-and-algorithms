# 1512. Number of Good Pairs

# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nhash = Counter(nums)
        count = 0
        for n in nhash.values():
            if n >1:
                count += (n*(n-1)/2)

        return int(count)