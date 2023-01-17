# 797. All Paths From Source to Target

# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

# sol 1: bfs
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q = deque([[0]])
        res = []
        n = len(graph)

        while q:
            path = q.popleft()
            u = path[-1]
            if u == n - 1:
                res.append(path)
                continue
            for m in graph[u]:
                q.append(path + [m])

        return res

# sol 2: dfs
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        def dfs(p):
            if p[-1] == len(graph) -1:
                res.append(p[:])
                return 
            for v in graph[p[-1]]:
                p.append(v)
                dfs(p)
                p.pop()
        
        dfs([0])
        return res
