# Description
# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed

    # set the flag for closed/open
    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) \
              + "]" if self.closed else "(" + str(self.start) + ", " \
              + str(self.end) + ")"
              
 def find_sets(intervals):
    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])
    s = e = 0
    res, count = 0, 0
    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        res = max(res, count)
    
    return res