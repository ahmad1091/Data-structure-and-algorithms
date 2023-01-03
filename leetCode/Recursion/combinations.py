# 77. Combinations

# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backTrack(i, sub):
            if len(sub) == k:
                res.append(sub.copy())
                return 

            for j in range(i, n+1):
                sub.append(j)
                backTrack(j+1, sub)
                sub.pop()  

        backTrack(1, [])

        return res