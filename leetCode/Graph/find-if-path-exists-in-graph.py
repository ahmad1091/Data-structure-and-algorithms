# 1971. Find if Path Exists in Graph

# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex source to vertex destination.

# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

 class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        chain = defaultdict(list)
        for a, b in edges:
            chain[a].append(b)
            chain[b].append(a)
        visit = set()
        def dfs(s):
            if s == destination:
                return True
            visit.add(s)
            for x in chain[s]:
                if x not in visit and dfs(x):
                    return True
            return False
        
        return dfs(source)
            