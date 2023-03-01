# 986. Interval List Intersections

# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

#  SOL :
 class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            s1, e1, s2, e2 = *firstList[i], *secondList[j]
            l, r = max(s1, s2), min(e1, e2)
            if l <= r:
                res.append([l, r])
            if e1 < e2:
                i += 1
            else:
                j += 1
            
        return res
            

#  sol 2: oop
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed

    # set the flag for closed/open
    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]" if self.closed else "(" + str(self.start) + ", " + str(self.end) + ")"

def intervals_intersection(interval_list_a, interval_list_b):
    intersections = []
    i = j = 0

    while i < len(interval_list_a) and j < len(interval_list_b):
        start = max(interval_list_a[i].start, interval_list_b[j].start)
        end = min(interval_list_a[i].end, interval_list_b[j].end)

        if start <= end:
            intersections.append(Interval(start, end))
            
        if interval_list_a[i].end < interval_list_b[j].end:
            i += 1
        else:
            j += 1

    return intersections
