# 207. Course Schedule

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preHash = {n:[] for n in range(numCourses)}

        for c, p in prerequisites:
            preHash[c].append(p)
        visit = set()
        def dfs(c):
            if c in visit:
                return False
            if preHash[c] == []:
                return True
            visit.add(c)
            for p in preHash[c]:
                if not dfs(p): return False
            visit.remove(c)
            preHash[c] = []
            return True

        for n in range(numCourses):
            if not dfs(n): return False
        return True