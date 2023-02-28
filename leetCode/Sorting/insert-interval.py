# 57. Insert Interval

# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res

# sol 2:
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_start, new_end = newInterval[0], newInterval[1]
        i, n = 0, len(intervals)

        while i < n and intervals[i][0] < new_start:
            res.append(intervals[i])
            i += 1
        if not res or new_start > res[-1][1]:
            res.append(newInterval)
        else:
            res[-1][1] = max(new_end, res[-1][1])

        while i < n:
            start, end = intervals[i]
            if start > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(end, res[-1][1])
            i += 1
            
        return res