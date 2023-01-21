# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        mx = 0

        for n in nums:
            if (n - 1) not in numSet:
                count = 0
                while n + count in numSet:
                    count += 1
                mx = max(count, mx)
        return mx