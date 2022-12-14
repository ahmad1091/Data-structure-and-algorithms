# 739. Daily Temperatures

# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indexOf = {n:i for i,n in enumerate(temperatures)}
        stack = []
        n = len(temperatures)
        res = [0] * n

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                val = stack.pop()
                res[val] += i - val
            stack.append(i)


        return res