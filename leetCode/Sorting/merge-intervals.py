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



# sol 2: same sol using oop:
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed
    # set the flag for closed/open

    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]" \
            if self.closed else \
                "(" + str(self.start) + ", " + str(self.end) + ")"

def merge_intervals(v):
    if not v:
        return None
    result = []
    result.append(Interval(v[0].start, v[0].end))
    for i in range(1, len(v)):
        last_added_interval = result[len(result) - 1]
        cur_start = v[i].start
        cur_end = v[i].end
        prev_end = last_added_interval.end
        if prev_end >= cur_start:
            last_added_interval.end = max(cur_end, prev_end)
        else:
            result.append(Interval(cur_start, cur_end))
    return result
