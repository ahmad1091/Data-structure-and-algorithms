# 547. Number of Provinces

# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

# sol 1: find-union
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        n = len(isConnected)
        par = list(range(n))
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    par[find(i)] = find(j)
        return sum([i == v for i, v in enumerate(par)])

sol 2: dfs 
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visit = set()
        res = 0
        
        def dfs(x):
            visit.add(x)
            for j in range(n):
                if j not in visit and isConnected[x][j]:
                    dfs(j)

        for x in range(n):
            if x not in visit:
                dfs(x)
                res += 1 

        return res