# 1863. Sum of All Subset XOR Totals

# The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

# For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
# Given an array nums, return the sum of all XOR totals for every subset of nums. 

# Note: Subsets with the same elements should be counted multiple times.

# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subSets = []

        def dfs(i, subset):
            if len(nums) <= i:
                if len(subset) > 0:
                    subSets.append(subset[:])
                return
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()
            dfs(i + 1, subset)

        dfs(0, [])
        
        total = 0
        for arr in subSets:
            res = arr[0]
            for n in arr[1:]:
                res ^= n
            total += res
                
        return total
