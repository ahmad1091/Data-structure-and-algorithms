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

# sol 2:
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []
        count = {n:0 for n in nums}

        for n in nums:
            count[n] +=1

        def dfs():
            if len(nums) == len(perm):
                result.append(perm[:])
                return

            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1

                    dfs()

                    count[n] += 1
                    perm.pop()
                    
        dfs()  
        return result