# 210. Course Schedule II

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            preReq[c].append(p)
        res = []
        visit, cycle = set(), set() 
        def dfs(c):
            if c in cycle: return False
            if c in  visit: return True
            
            cycle.add(c)
            for p in preReq[c]:
                if not dfs(p): return False

            cycle.remove(c)
            visit.add(c)
            res.append(c)
            return True

        for c in range(numCourses):
            if not dfs(c): return []

        return res
            