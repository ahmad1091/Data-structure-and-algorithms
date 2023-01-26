# 1203. Sort Items by Groups Respecting Dependencies

# There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

# Return a sorted list of the items such that:

# The items that belong to the same group are next to each other in the sorted list.
# There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
# Return any solution if there is more than one solution and return an empty list if there is no solution.

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topoSort(nodes, graph, inDegree):
            q = deque([node for node in nodes if node not in inDegree])

            res = []
            while q:
                cur = q.popleft()
                res.append(cur)
                    
                for e in graph[cur]:
                    inDegree[e] -= 1
                    if inDegree[e] == 0:
                        q.append(e)
            return res
        
        groupItems = defaultdict(list)
        groupId = m
        for i in range(n):
            if group[i] == -1:
                group[i] = groupId
                groupId += 1
            groupItems[group[i]].append(i)

        itemGraph = defaultdict(list)
        itemInDegree = defaultdict(int)

        for v, u_list in enumerate(beforeItems):
            for u in u_list:
                if group[u] == group[v]:
                    itemGraph[u].append(v)
                    itemInDegree[v] += 1

        sortedGroupItems = {}
        for groupId in groupItems:
            sortedItems = topoSort(groupItems[groupId], itemGraph, itemInDegree)

            if len(sortedItems) != len(groupItems[groupId]): return []
            sortedGroupItems[groupId] = sortedItems

        groupGraph = defaultdict(list)
        groupInDegree = defaultdict(int)

        for v, u_list in enumerate(beforeItems):
            for u in u_list:
                if group[v] != group[u]:
                    groupGraph[group[u]].append(group[v])
                    groupInDegree[group[v]] += 1

        groups = set(group)
        sortedGroups = topoSort(groups, groupGraph, groupInDegree)

        if len(groups) != len(sortedGroups): return []

        res = []
        for groupId in sortedGroups:
            res.extend(sortedGroupItems[groupId])
        
        return res 
