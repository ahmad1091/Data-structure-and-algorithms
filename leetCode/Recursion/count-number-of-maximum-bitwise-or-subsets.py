# 2044. Count Number of Maximum Bitwise-OR Subsets

# Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.

# The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
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
        ored = []
        mx = float('-inf')
        for arr in subSets:
            res = arr[0]
            for n in arr[1:]:
                res |= n
            ored.append(res)
            mx = max(mx, res)

        count = 0
        for o in ored:
            if o == mx:
                count += 1

        return count


# sol 2: cleaner code 
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx = ans = 0
        for x in nums:
            mx |= x

        def dfs(i, t):
            nonlocal mx, ans
            if i == len(nums):
                if t == mx:
                    ans += 1
                return
            dfs(i + 1, t)
            dfs(i + 1, t | nums[i])

        dfs(0, 0)
        return ans

