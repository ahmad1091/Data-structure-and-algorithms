# 2367. Number of Arithmetic Triplets

# You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

# i < j < k,
# nums[j] - nums[i] == diff, and
# nums[k] - nums[j] == diff.
# Return the number of unique arithmetic triplets.

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        numSet = set(nums)
        total = 0
        for n in numSet:
            if (n - diff) in numSet and (n - 2 * diff) in numSet:
                total += 1
        
        return total