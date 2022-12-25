# 56. Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda intervals : intervals[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            prevEnd = res[-1][1] 
            if start <=  prevEnd:
                res[-1][1] = max(prevEnd, end)
            else:
                res.append([start, end])

        return res



