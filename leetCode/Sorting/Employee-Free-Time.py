# Description
# We are given a list schedule of employees, which represents the working time for each employee.

# Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

# Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

# (Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

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

def employee_free_time(schedule):  
    result = []
    intervals = []
    for s in schedule:
        intervals.extend(s)
        print(intervals)
    intervals.sort(key = lambda x: x.start)

    prev_end = intervals[0].end
    for i in intervals:
        if prev_end < i.start:
            result.append(Interval(prev_end, i.start))
        prev_end = max(prev_end, i.end)
        
    return result