# 47. Permutations II

# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

# Sol 1: from first Permutations problem but using set 
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permuteUnique(nums)

            for p in perms:
                p.append(n)
            
            result.extend(perms)
            nums.append(n)

        arr = set(tuple(x) for x in result)
        return list(list(x) for x in arr)