# Permutations with Dups: Write a method to compute all permutations of a string whose charac-
# ters are not necessarily unique. The list of permutations should not have duplicates.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for p in perms:
                p.append(n)
            
            result.extend(perms)
            nums.append(n)

        return result