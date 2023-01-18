# 841. Keys and Rooms

# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

# When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

# sol 1: dfs
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(room):
            if room in visited:
                return 
            visited.add(room)
            for r in rooms[room]:
                dfs(r)
        dfs(0)
        return len(rooms) == len(visited)


# sol 2: bfs 
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        key_q = deque([0])
        visited = set(key_q)

        while key_q:
            key = key_q.popleft()
            for room in rooms[key]:
                if room not in visited:
                    key_q.append(room)
                    visited.add(room)

        return len(visited) == len(rooms)